from django.urls import path
from . import views


urlpatterns = [
    path('', views.CategoryList.as_view(), name='home'),
    path('articles/', views.PostList.as_view(), name='articles'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='article_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('category/<category>/', views.CatListView.as_view(), name='category'),
    path('profile/', views.MyProfile.as_view(), name='profile'),
]
