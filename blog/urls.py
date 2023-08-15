from django.urls import path

from . import views


urlpatterns = [
    path('articles/', views.PostList.as_view(), name='articles'),
]
