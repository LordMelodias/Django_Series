from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
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
    return render(request, 'project_detail.html', {'project': project})

# API Views
class ProjectListCreateView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # 

class ProjectDetailView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


@api_view(['POST'])
def comment_project(request, pk):
    print("COmment:",request.data)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        project = Project.objects.get(pk=pk)
        print("Project:",project)
        serializer.save(project=project)
        return redirect('project-detail', pk=pk)
    return Response(serializer.errors, status=400)
