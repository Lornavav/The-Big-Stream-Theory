from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.text import slugify
from allauth.account.views import LoginView
from .models import Post, Category
from .forms import CommentForm, BlogForm


class PostList(generic.ListView):
    """
    View to show all articles on articles page
    will paginate after 6 posts
    only published posts will appear
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'articles.html'
    paginate_by = 6


# Inspiration taken from https://project4-cocktail-nerd.herokuapp.com/
class CategoryList(generic.ListView):
    """
    View to return all categories created on the back end
    """

    model = Category
    template_name = 'index.html'

    def get_queryset(self):
        category_list = Category.objects.all()
        return category_list


class CatListView(ListView):
    """
    View to return articles by category when
    user has clicked on a category
    """

    template_name = 'category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(
                category__name=self.kwargs['category']).filter(status=1)
        }
        return content


# Followed codestar CI walkthrough to create this view
class PostDetail(View):
    """
    View to display page for single article
    including comment feature
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "article_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "article_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class PostLike(View):
    """
    View to handle end user liking/unliking articles
    """

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('article_detail', args=[slug]))


@login_required
def add_article(request):
    """
    View for staff to create a new article on the front end
    Published articles will display on front end
    Draft articles will display on admin side
    """
    submitted = False
    if request.method == 'POST':

        form = BlogForm(request.POST, request.FILES)
        if all([form.is_valid()]):
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            messages.success(
                request,
                'Your article was submitted successfully!'
            )
            return HttpResponseRedirect('/add_post?submitted=True')
    else:
        form = BlogForm
        if 'submitted' in request.GET:
            submitted = True

    return render(
        request, 'add_post.html', {'form': form, 'submitted': submitted})


class EditPost(SuccessMessageMixin, UpdateView):
    """
    Staff can edit articles
    """
    model = Post
    form_class = BlogForm
    template_name = 'edit_post.html'
    success_message = 'The article was edited successfully!'
    success_url = reverse_lazy('articles')


class DeletePost(DeleteView):
    """
    Staff can delete posts
    """
    model = Post
    template_name = 'delete_post.html'
    success_message = "The article was successfully deleted!"
    success_url = reverse_lazy('articles')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeletePost, self).delete(request, *args, **kwargs)
