"""
Organizational Models for grouping surveys and users.
Includes:
    -
    -
    -
"""
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Organization(models.Model):
    """
    Organizations are used to group users and centralise survey ownership
    """
    org_name = models.CharField(
        max_length=255, blank=False, null=False, primary_key=True)
    org_comment = models.CharField(max_length=511, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.org_name)


class Profile(models.Model):
    """
    Profile links users to corresponding Organizations
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    org = models.ForeignKey(
        to=Organization, on_delete=models.CASCADE, blank=True, null=True)
    can_create_org = models.BooleanField(default=False, null=False, blank=False)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Creates a User's Profile upon User activation
    """
    if created:
        Profile.objects.create(user=instance)
