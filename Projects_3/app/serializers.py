from rest_framework import serializers
from .models import Project, ProjectImage, Comment

class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ['id', 'image']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True, default=None)  # Allow null user

    class Meta:
        model = Comment
        fields = ['id', 'user', 'content', 'created_at']

class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'image', 'technologies_used', 
                  'issues_faced', 'created_at', 'images', 'comments']

    def get_likes_count(self, obj):
        return obj.likes.count()