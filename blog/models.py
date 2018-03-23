from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogPost(models.Model):
    blog_title = models.CharField(max_length=128)
    blog_text = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
    blog_author = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.blog_title + " (" + self.pub_date.strftime("%Y-%m-%d %H:%M:%S") + ")"
