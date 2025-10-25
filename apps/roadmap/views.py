from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.forms import modelformset_factory

from .models import Category, Phase, Topic, Project, TopicProgress, ProjectProgress
from .forms import TopicProgressForm

def roadmap_view(request):
    """Display the complete roadmap with progress"""
    categories = Category.objects.prefetch_related(
        'phases__topics',
        'phases__projects'
    ).all()

    # Collect all topics to be displayed so we can build a formset
    topic_qs = Topic.objects.select_related('phase__category').all()

    # If user is authenticated, prepare a ModelFormSet to show/edit TopicProgress rows
    topic_forms_map = {}
    topic_formset = None
    if request.user.is_authenticated:
        # get existing progress for displayed topics
        existing_qs = TopicProgress.objects.filter(user=request.user, topic__in=topic_qs)

        # determine missing topics
        existing_topic_ids = set(existing_qs.values_list('topic_id', flat=True))
        missing_topics = [t for t in topic_qs if t.id not in existing_topic_ids]

        # create formset class with extra forms for missing topics
        extra = len(missing_topics)
        TopicProgressFormSet = modelformset_factory(TopicProgress, form=TopicProgressForm,
                                                    fields=('topic', 'completed'), extra=extra)

        initial = [{'topic': t.id, 'completed': False} for t in missing_topics]

        if request.method == 'POST':
            formset = TopicProgressFormSet(request.POST, queryset=existing_qs)
            if formset.is_valid():
                instances = formset.save(commit=False)
                # save or update instances, ensure user is set
                for inst in instances:
                    if not inst.pk:
                        inst.user = request.user
                    inst.save()
                # there may be deletes/other instances; ensure all saved
                return redirect('roadmap:roadmap')
        else:
            formset = TopicProgressFormSet(queryset=existing_qs, initial=initial)

        # Build mapping topic_id -> form for simple rendering by topic
        for form in formset:
            topic_id = None
            if form.instance and getattr(form.instance, 'topic_id', None):
                topic_id = form.instance.topic_id
            else:
                topic_id = form.initial.get('topic')
            if topic_id:
                topic_forms_map[int(topic_id)] = form

        topic_formset = formset

        # Progress lists for quick checks (used for projects display)
        project_progress = ProjectProgress.objects.filter(
            user=request.user
        ).values_list('project_id', flat=True)
    else:
        topic_formset = None
        topic_forms_map = {}
        project_progress = []

    # Build a nested structure so templates can iterate and show forms next to each topic
    categories_with_forms = []
    for category in categories:
        cat_entry = {'category': category, 'phases': []}
        for phase in category.phases.all():
            phase_entry = {'phase': phase, 'topics': [], 'projects': phase.projects.all()}
            for topic in phase.topics.all():
                phase_entry['topics'].append({'topic': topic, 'form': topic_forms_map.get(topic.id)})
            cat_entry['phases'].append(phase_entry)
        categories_with_forms.append(cat_entry)

    context = {
        'categories_with_forms': categories_with_forms,
        'topic_formset': topic_formset,
        'project_progress': project_progress,
    }
    return render(request, 'roadmap/roadmap.html', context)


@login_required
def toggle_project_progress(request):
    """AJAX view to toggle project completion status"""
    if request.method == 'POST':
        project_id = request.POST.get('project_id')
        github_link = request.POST.get('github_link', '')
        progress, created = ProjectProgress.objects.get_or_create(
            user=request.user,
            project_id=project_id
        )
        if not created:
            progress.completed = not progress.completed
        progress.github_link = github_link
        progress.save()
        return JsonResponse({
            'status': 'success',
            'completed': progress.completed
        })
    return JsonResponse({'status': 'error'}, status=400)