from django.urls import path
from . import views


urlpatterns = [
    path('', views.CategoryList.as_view(), name='home'),
    path('articles/', views.PostList.as_view(), name='articles'),
]
