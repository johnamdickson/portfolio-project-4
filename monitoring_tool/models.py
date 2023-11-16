from django.db import models
from django.contrib.auth.models import User, Group
import constants as k
from datetime import timedelta, datetime, timezone
from dateutil.relativedelta import relativedelta
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
import cloudinary.api
from django.utils.text import slugify
import json
from django.core.validators import FileExtensionValidator


class Emission(models.Model):
    type_choices = k.EMISSION_TYPES
    status_choices = k.STATUS
    title = models.CharField(max_length=20, unique=True)
    location = models.CharField(max_length=50, unique=False)
    slug = models.SlugField(max_length=200, unique=True)
    username = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="monitoring_tool_emissions"
    )
    emission_image = CloudinaryField(
        'image', null=False, resource_type='auto',
        format="jpg"
        )
    description = models.TextField(max_length=100, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_checked = models.DateField(auto_now=False)
    next_check_due = models.DateField(auto_now=False)
    current_check_due = models.DateField(auto_now=False)
    status = models.IntegerField(choices=status_choices, default=0)
    type = models.IntegerField(choices=type_choices, default=0)
    close_out_comments = models.TextField(max_length=100, blank=True)
    closed_by = models.CharField(max_length=30, unique=False, blank=True)
    close_out_date = models.DateTimeField(auto_now_add=False, blank= True, null=True)

# solution to accessing strings values from choices tuple:
# https://stackoverflow.com/questions/60556709/how-do-i-get-the-string-value-of-the-tuple-in-django
    def get_emission_type(self):
        """
        Function to acess string values 
        from choices tuple.
        """
        return dict(self.type_choices).get(self.type)
    
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def calculate_check_complete(self):
        """
        Function to return a check completion string 
        representation using the status number.
        """
        if self.current_check_due <= self.last_checked <= self.next_check_due:
            return "Checks Complete"
        else:
            return "Checks Outstanding"

    def calculate_status(self):
        """
        Function to return a emission status string 
        representation using the status number.
        """
        if self.status == 0:
            return "Open"
        else:
            return "Closed"

    def javascript_data(self):
        """
        Function returns a json of the model instance values
        for use in javascript.
        """
        list = {"title": self.title, 
                "location": self.location, 
                "username": str(self.username),
                "checkComplete": self.calculate_check_complete(),
                "imageUrl": self.emission_image.url,
                "description": self.description,
                "latitude": self.latitude,
                "longitude": self.longitude,
                "created": str(self.created_on),
                "lastCheck": str(self.last_checked),
                "nextCheck": str(self.next_check_due),
                "currentCheck": str(self.current_check_due),
                "status": self.calculate_status(),
                "type": self.get_emission_type(),
                "slug": self.slug}
        return json.dumps(list)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class EmissionCheck(models.Model):
    title = models.ForeignKey(Emission, on_delete=models.CASCADE,
                              related_name="emissioncheck")
    date_checked = models.DateTimeField(auto_now=False)
    status = models.IntegerField(choices=k.CHECK_STATUS, default=0)
    comments = models.TextField(max_length=100)
    checked_by = models.ForeignKey(
        User, on_delete=models.RESTRICT
    )
    edit_comments = models.TextField(max_length=100, blank=True)
    edited_by = models.CharField(max_length=30, unique=False, blank=True)
    edit_date = models.DateTimeField(auto_now_add=False, blank= True, null=True)
    
    # Bug with dattime comparisons can't "compare offset-naive and offset-aware datetimes"
    # solution from stack overflow:
    # https://stackoverflow.com/questions/796008/cant-subtract-offset-naive-and-offset-aware-datetimes
    def check_less_than_24_hours (self):
        """
        Function to determine if the check 
        is less than 24 hours since submitted.
        """
        now_aware = datetime.now(timezone.utc)
        return now_aware < self.date_checked + timedelta(days=1)

    def calculate_status(self):
        """
        Function to return a status string 
        representation using the status number.
        """
        if self.status == 1:
            return "No Emission Detected"
        elif self.status ==2:
            return "Below Minimum Threshold"
        elif self.status ==3:
            return "Above Minimum Threshold"


# selection of user group on registration, solution from Stack Overflow:
# https://stackoverflow.com/questions/48544176/how-to-set-default-group-for-new-user-in-django
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        instance.groups.add(Group.objects.get(name='emission_user'))
