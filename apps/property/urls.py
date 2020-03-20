
from django.urls import  re_path

from . import views

urlpatterns = [
    re_path(r'add_property', views.AddProperty.as_view()),

]


