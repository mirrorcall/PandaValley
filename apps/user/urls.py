from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'join', views.JoinView.as_view()),
    re_path(r'login', views.LoginView.as_view()),
    re_path(r'forget_password', views.ForgetPassword.as_view()),
    re_path(r'email_validation', views.EmailValidation.as_view()),
    re_path(r'reset_password', views.ResetPassword.as_view()),
    re_path(r'upload_avatar', views.UploadAvatarView.as_view()),
    re_path(r'pass_user_info', views.PassUserInfoView.as_view()),
    re_path(r'modify_user_info', views.ModifyProfileView.as_view()),
    re_path(r'emailvalidation', views.EmailValidation.as_view())
]
