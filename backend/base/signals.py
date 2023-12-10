from django.db.models.signals import pre_save #'pre_save' is a signal that is sent before saving a model instance
from django.contrib.auth.models import User
# from django.dispatch import receiver


def updateUser(sender, instance, **kwargs):
    user = instance
    if user.email != '':
        user.username = user.email #if the user has an email, then set the username to the email

pre_save.connect(updateUser, sender=User) #connect the signal to the function