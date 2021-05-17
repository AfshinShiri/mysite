from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


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



