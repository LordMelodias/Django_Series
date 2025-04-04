from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import userProfile
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.


def authView(request):
    return render(request, 'auth.html')

def homeView(request):
    # Example: Pass User-Agent to template (optional)
    user_agent = getattr(request, 'user_agent', 'Unknown')
    user_agent = user_agent.lower()
    print("user: ", user_agent)
    if 'windows' in user_agent:
        device='Windows'
    elif 'macintosh' in user_agent or 'mac os' in user_agent:
        device='Mac'
    elif 'iphone' in user_agent:
        device='iPhone'
    elif 'ipad' in user_agent:
        device= 'iPad'
    elif 'android' in user_agent:
        device= 'Android'
    elif 'linux' in user_agent:
        device= 'Linux'
    else:
        device= 'Unknown'
    return render(request, 'home.html', {'device': device})

@api_view(['POST'])
def registerView(request):
    username = request.data.get("username")
    email = request.data.get("email")
    mobile = request.data.get("mobile")
    password = make_password(request.data.get("password"))
    if not mobile or not email or not password or not username:
        return Response({"error": "Missing Required Field"}, status=status.HTTP_400_BAD_REQUEST)
    user = userProfile.objects.create(username=username, email=email, mobile=mobile, password=password)
    return Response({"message": "User Registered Successfully"}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def loginView(request):
    print("it come")
    email = request.data.get("email")
    password = request.data.get("password")
    print("email", email, password)
    try:
        user = userProfile.objects.get(email=email)  # Use get() to retrieve a single user
        print("user", user)
    except userProfile.DoesNotExist:
        return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)
    if check_password(password, user.password):
        # Return more user details for the home page
        print("it check")
        return Response({
                "email": user.email
                }, status=status.HTTP_200_OK)
    return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getUserProfile(request):
    email = request.query_params.get("email")
    try:
        user = userProfile.objects.get(email=email)
        return Response({
            "username": user.username,
            "email": user.email,
            "mobile": user.mobile,
            "profile_image": user.profile_image.url if user.profile_image else None
        }, status=status.HTTP_200_OK)
    except userProfile.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def updateProfileImage(request):
    email = request.data.get("email")
    try:
        user = userProfile.objects.get(email=email)
        if 'profile_image' in request.FILES:
            user.profile_image = request.FILES['profile_image']
            user.save()
            return Response({
                "message": "Profile image updated successfully",
                "profile_image": user.profile_image.url
            }, status=status.HTTP_200_OK)
        return Response({"error": "No image provided"}, status=status.HTTP_400_BAD_REQUEST)
    except userProfile.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)