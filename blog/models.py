from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# users - authors of the post
# posts
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # to see sql statement run in the migration
    # python manage.py sqlmigrate blog 0001   --- appname and migration number
    def __str__(self):
        return self.title