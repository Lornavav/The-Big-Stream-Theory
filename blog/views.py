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
from .models import Post, Category, Profile
from .forms import CommentForm, UserUpdateForm, ProfileUpdateForm, BlogForm


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


class CatListView(ListView):

    template_name = 'category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(
                category__name=self.kwargs['category']).filter(status=1)
        }
        return content


class PostDetail(View):

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

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('article_detail', args=[slug]))


@login_required
def profile(request):

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES,
            instance=request.user.profile
        )

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(
                request, 'Your profile has been updated successfully!')
            return redirect(to='profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def show_all_users(request):
    """
    Get all user profile data and make it available site wide
    """
    data = Profile.objects.all()

    context = {
        'data': data
    }
    return context


class CreateArticle(View):

    def get(self, request):
        if self.request.user.is_authenticated:
            form = BlogForm()
            context = {'form': form}

            return render(request, 'add_post.html', context)

        else:
            return redirect('articles')

    def post(self, request, *arg, **kwargs):
        print(self.request.user.id)
        if self.request.user.is_authenticated:
            form = BlogForm(request.POST)
            if form.is_valid():

                form.instance.author = self.request.user
                form.instance.slug = slugify(form.instance.title)

                new_entry = form.save()
                messages.success(request, f"{new_entry} was successfully added!")

                return redirect('article_detail', new_entry.slug)
            else:
                return render(request, 'add_post.html', {'form': form})

        else:
            return redirect('home')


class EditPost(SuccessMessageMixin, UpdateView):
    model = Post
    form_class = BlogForm
    template_name = 'edit_post.html'
    success_message = 'The article was edited successfully!'
    success_url = reverse_lazy('articles')


class DeletePost(DeleteView):

    model = Post
    template_name = 'delete_post.html'
    success_message = "The article was successfully deleted!"
    success_url = reverse_lazy('articles')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeletePost, self).delete(request, *args, **kwargs)

