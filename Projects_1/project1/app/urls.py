# urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.authView, name='auth'),
    path('home/', views.homeView, name='home'),
    path('register/', views.registerView, name='register'),
    path('login/', views.loginView, name='login'),
    path('home/user-profile/', views.getUserProfile, name='get_user_profile'),
    path('home/update-profile-image/', views.updateProfileImage, name='update_profile_image'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)