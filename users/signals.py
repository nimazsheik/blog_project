from django.db.models.signals import post_save
# signal that fired after an object is saved(when user created
from django.contrib.auth.models import User
# sender will be sending the signal - User
from django.dispatch import receiver
from .models import Profile


# we want user profile to be created for each user
@receiver(post_save,sender=User)
def create_profile(sender,instance,created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# saves profile everytime user gets saved
@receiver(post_save,sender=User)
def save_profile(sender,instance, **kwargs):
    instance.profile.save()