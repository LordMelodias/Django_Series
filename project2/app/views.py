# call_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Call
from .serializers import UserSerializer, CallSerializer
from django.core.cache import cache


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Token.objects.get_or_create(user=user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            Token.objects.get_or_create(user=user)
            return redirect('user_list')
    return render(request, 'login.html')

@login_required
def user_list_view(request):
    token = Token.objects.get(user=request.user).key
    return render(request, 'user_list.html', {'token': token})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_users(request):
    users = User.objects.exclude(id=request.user.id)
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def make_call(request):
    receiver_id = request.data.get('receiver_id')
    receiver = User.objects.get(id=receiver_id)
    call = Call.objects.create(caller=request.user, receiver=receiver)
    serializer = CallSerializer(call)
    return Response({"message": f"Calling {receiver.username}", "call": serializer.data})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def hangup_call(request):
    receiver_id = request.data.get('receiver_id')
    user_id = request.user.id
    # Set hangup signal
    cache.set(f"call_status_{user_id}_{receiver_id}", 'hangup', timeout=30)
    cache.set(f"call_status_{receiver_id}_{user_id}", 'hangup', timeout=30)
    return Response({'status': 'hangup_signal_sent'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def call_status(request):
    user_id = request.user.id
    active_call_key = request.GET.get('active_call_key', None)
    if active_call_key:
        status = cache.get(active_call_key)
        if status == 'hangup':
            other_user_id = int(active_call_key.split('_')[2]) if user_id == int(active_call_key.split('_')[3]) else int(active_call_key.split('_')[3])
            # Clear the cache entries once hangup is detected
            cache.delete(active_call_key)
            cache.delete(f"call_status_{other_user_id}_{user_id}")
            return Response({'status': 'hangup', 'user_id': other_user_id})
    return Response({'status': 'active'})