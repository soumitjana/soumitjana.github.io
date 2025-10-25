from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Phase(models.Model):
    category = models.ForeignKey(Category, related_name='phases', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    week_range = models.CharField(max_length=50)
    goal = models.TextField()
    order = models.IntegerField()
    
    class Meta:
        ordering = ['category', 'order']

    def __str__(self):
        return f"Phase {self.order}: {self.title}"

class Topic(models.Model):
    phase = models.ForeignKey(Phase, related_name='topics', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.name

class Project(models.Model):
    phase = models.ForeignKey(Phase, related_name='projects', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.name

class Resource(models.Model):
    RESOURCE_TYPES = [
        ('BOOK', 'Book'),
        ('COURSE', 'Course'),
        ('ONLINE', 'Online Resource')
    ]
    
    title = models.CharField(max_length=200)
    resource_type = models.CharField(max_length=20, choices=RESOURCE_TYPES)
    url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    phases = models.ManyToManyField(Phase, related_name='resources')
    
    def __str__(self):
        return self.title

class TopicProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['user', 'topic']
    
    def __str__(self):
        return f"{self.user.username} - {self.topic.name} - {'Completed' if self.completed else 'In Progress'}"

class ProjectProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(auto_now=True)
    github_link = models.URLField(blank=True)
    
    class Meta:
        unique_together = ['user', 'project']
    
    def __str__(self):
        return f"{self.user.username} - {self.project.name} - {'Completed' if self.completed else 'In Progress'}"