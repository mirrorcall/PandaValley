
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    re_path(r'join', views.JoinView.as_view()),
    re_path(r'login', views.LoginView.as_view()),
    re_path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name='password_change_done'),

    re_path('password_change/', auth_views.PasswordChangeView.as_view(template_engine='registration/password_change.html'),
         name='password_change'),

    re_path('password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_engine='registration/password_reset_done.html'),
         name='password_reset_done'),

    re_path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    re_path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    re_path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_engine='registration/password_reset_complete.html'),
         name='password_reset_complete'),
]