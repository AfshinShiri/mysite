from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('published','Published'),)

    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250, unique_for_date='publish')
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    create = models.DateTimeField(auto_now_add=True)     #tarihe ijad
    update = models.DateTimeField(auto_now=True)         #tarikhe lahze update
    publish = models.DateTimeField(default=timezone.now) #tarikhe enteshar---timezone lahze knonie enteshar
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default= 'draft')

    objects = models.Manager() # mangere default
    published = PublishedManager() # manage khodemon

    class Meta: #vahti queryset mizanim akharin poste enteshari ro aval namayesh mide
        ordering = ('-publish',)

    def __str__(self): #namayeshe stringi az post
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f"comment by {self.name} on {self.post}"




