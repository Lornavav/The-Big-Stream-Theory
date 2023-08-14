from .import views
from django.urls import path


urlpatterns = [
    path('articles/', views.PostList.as_view(), name='articles')
]