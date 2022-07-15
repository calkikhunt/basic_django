from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('projects/', views.projects),
    path('project/<str:project_id>/', views.project),
]