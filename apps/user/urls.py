
from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'join', views.JoinView.as_view()),
    re_path(r'login', views.LoginView.as_view()),
    re_path(r'forgetpassword',views.ForgetPassword.as_view()),
    re_path(r'emailvalidation',views.EmailValidation.as_view()),
    re_path(r'resetpassword',views.ResetPassword.as_view())
]