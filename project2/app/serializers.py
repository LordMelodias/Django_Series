from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Call

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class CallSerializer(serializers.ModelSerializer):
    caller = UserSerializer(read_only=True)
    receiver = UserSerializer(read_only=True)

    class Meta:
        model = Call
        fields = ['id', 'caller', 'receiver', 'timestamp']