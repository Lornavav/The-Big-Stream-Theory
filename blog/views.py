from django.shortcuts import render
from django.views import generic, View
from .models import Post, Category


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(
        status=1).order_by('-created_on')
    template_name = 'articles.html'
    paginate_by = 6


class CategoryList(generic.ListView):

    model = Category
    template_name = 'index.html'
    
    def get_queryset(self):
        category_list = Category.objects.all()
        return category_list
