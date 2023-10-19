from django.db import models
from django.contrib.auth.models import User, Group
import constants as k
from django.db.models.signals import post_save
from django.dispatch import receiver


class Emission(models.Model):
    title = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=50, unique=False)
    slug = models.SlugField(max_length=200, unique=True)
    username = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="monitoring_tool_emissions"
    )
    description = models.TextField(blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField() 
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    next_check_due = models.DateField(auto_now=False)
    current_check_due = models.DateField(auto_now=False)
    status = models.IntegerField(choices=k.STATUS, default=0)
    type = models.IntegerField(choices=k.EMISSION_TYPES, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


class EmissionCheck(models.Model):
    title = models.ForeignKey(Emission, on_delete=models.CASCADE,
                              related_name="emissioncheck")
    date_checked = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=k.CHECK_STATUS, default=0)
    comments = models.TextField()
    checked_by = models.ForeignKey(
        User, on_delete=models.RESTRICT
    )


# selection of user group on registration, solution from Stack Overflow:
# https://stackoverflow.com/questions/48544176/how-to-set-default-group-for-new-user-in-django
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        instance.groups.add(Group.objects.get(name='emission_user'))