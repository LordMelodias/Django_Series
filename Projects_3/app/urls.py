from django.urls import path
from .views import (home, project_detail, ProjectListCreateView, 
                    ProjectDetailView, CommentProjectView)

urlpatterns = [
    # Frontend URLs
    path('', home, name='home'),
    path('projects/<int:pk>/', project_detail, name='project-detail'),
    
    # API URLs
    path('projects/', ProjectListCreateView.as_view(), name='project-list'),
    path('projects/<int:pk>/api/', ProjectDetailView.as_view(), name='project-detail-api'),
    path('projects/<int:pk>/comment/', CommentProjectView.as_view(), name='project-comment'),
]