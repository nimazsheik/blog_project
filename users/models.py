from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        # return how we want this to be displaed
        return f'{self.user.username} Profile'
        # when we print profile, it will print 'Nimaz Profile'
        # to work with images run Pillow(library)