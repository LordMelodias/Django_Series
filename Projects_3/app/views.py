from django.shortcuts import render, redirect
from django.urls import reverse
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Project, Comment
from .serializers import ProjectSerializer, CommentSerializer

# Frontend Views
def home(request):
    web_projects = Project.objects.filter(category='web')
    data_projects = Project.objects.filter(category='data')
    cloud_projects = Project.objects.filter(category='cloud')
    return render(request, 'home.html', {
        'web_projects': web_projects,
        'data_projects': data_projects,
        'cloud_projects': cloud_projects,
    })
    
    
def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    if request.method == 'POST' and 'content' in request.POST:
        Comment.objects.create(
            user=request.user if request.user.is_authenticated else None,
            project=project,
            content=request.POST['content']
        )
        return redirect('project-detail', pk=pk)
    return render(request, 'project_detail.html', {'project': project})

# API Views
class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]

class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.AllowAny]


class CommentProjectView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]  # Explicitly allow anyone

    def perform_create(self, serializer):
        project = Project.objects.get(pk=self.kwargs['pk'])
        serializer.save(
            user=self.request.user if self.request.user.is_authenticated else None,
            project=project
        )

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return redirect('project-detail', pk=self.kwargs['pk'])
