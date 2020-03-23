from django.urls import path, re_path

from . import views
urlpatterns = [
    re_path(r'search', views.Search.as_view()),

]
