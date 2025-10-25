from django.contrib import admin
from . import models


class TopicInline(admin.TabularInline):
	model = models.Topic
	extra = 0


class ProjectInline(admin.TabularInline):
	model = models.Project
	extra = 0


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'code', 'order')
	ordering = ('order',)
	inlines = []


@admin.register(models.Phase)
class PhaseAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'order')
	list_filter = ('category',)
	inlines = [TopicInline, ProjectInline]


@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
	list_display = ('name', 'phase', 'order')
	list_filter = ('phase__category',)


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ('name', 'phase', 'order')
	list_filter = ('phase__category',)


@admin.register(models.Resource)
class ResourceAdmin(admin.ModelAdmin):
	list_display = ('title', 'resource_type')
	filter_horizontal = ('phases',)


@admin.register(models.TopicProgress)
class TopicProgressAdmin(admin.ModelAdmin):
	list_display = ('user', 'topic', 'completed', 'completed_at')
	list_filter = ('completed', 'user')


@admin.register(models.ProjectProgress)
class ProjectProgressAdmin(admin.ModelAdmin):
	list_display = ('user', 'project', 'completed', 'completed_at')
	list_filter = ('completed', 'user')
