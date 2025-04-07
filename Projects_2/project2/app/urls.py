from django.urls import path
from . import views

urlpatterns = [
    path('api/users/', views.get_users, name='get_users'),
    path('api/call/', views.make_call, name='make_call'),
    path('api/call/hangup/', views.hangup_call, name='hangup_call'),  # Correct endpoint for hangup
    path('api/call/status/', views.call_status, name='call_status'),  # Add status endpoint
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('users/', views.user_list_view, name='user_list'),
]