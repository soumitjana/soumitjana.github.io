from django.urls import path
from . import views

app_name = 'roadmap'

urlpatterns = [
    path('', views.roadmap_view, name='roadmap'),
    #path('toggle-topic/', views.toggle_topic_progress, name='toggle_topic'),
    path('toggle-project/', views.toggle_project_progress, name='toggle_project'),
]