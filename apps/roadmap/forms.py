from django import forms
from django.forms import ModelForm
from .models import TopicProgress, Topic


class TopicProgressForm(ModelForm):
    class Meta:
        model = TopicProgress
        fields = ['topic', 'completed']
        widgets = {
            'topic': forms.HiddenInput(),
            'completed': forms.CheckboxInput(attrs={'class': 'topic-checkbox-input'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Show topic name next to the checkbox in template via form.topic_name
        topic_obj = None
        if self.instance and getattr(self.instance, 'topic', None):
            topic_obj = self.instance.topic
        else:
            topic_id = self.initial.get('topic')
            if topic_id:
                try:
                    topic_obj = Topic.objects.get(pk=topic_id)
                except Topic.DoesNotExist:
                    topic_obj = None
        self.topic_name = topic_obj.name if topic_obj else ''
