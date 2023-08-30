from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    """
    Category model
    """
    name = models.CharField(max_length=50, unique=True)
    category_image = CloudinaryField('image', default='placeholder')

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Post model for admins to create articles for the website
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cast = models.CharField(max_length=300)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """
    Comments Model
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(
        default='avatar.jpg',
        upload_to='profile_avatars'
    )

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)

            img.thumbnail(output_size)

            img.save(self.avatar.path)
