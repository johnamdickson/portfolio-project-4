from django.db import models
from django.contrib.auth.models import User, Group
import constants as k
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
    title = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=50, unique=False)
    slug = models.SlugField(max_length=200, unique=True)
    username = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="monitoring_tool_emissions"
    )
    # use of FileExtensionValidator form this source:
    # https://www.geeksforgeeks.org/fileextensionvalidator-validate-file-extensions-in-django/
    emission_image = CloudinaryField(
        'image', null=False, resource_type='auto',
        format="jpg"
        )
    description = models.TextField(blank=True)
    close_out_comments = models.TextField(blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_checked = models.DateField(auto_now=True)
    next_check_due = models.DateField(auto_now=False)
    current_check_due = models.DateField(auto_now=False)
    status = models.IntegerField(choices=status_choices, default=0)
    type = models.IntegerField(choices=type_choices, default=0)

# solution to accessing strings values from choices tuple:
# https://stackoverflow.com/questions/60556709/how-do-i-get-the-string-value-of-the-tuple-in-django
    def get_emission_type(self):
        return dict(self.type_choices).get(self.type)
    
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def calculate_check_complete(self):
        if self.current_check_due <= self.last_checked <= self.next_check_due:
            return "Checks Complete"
        else:
            return "Checks Outstanding"

    def calculate_status(self):
        if self.status == 0:
            return "Open"
        else:
            return "Closed"

    def javascript_data(self):
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
    date_checked = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=k.CHECK_STATUS, default=0)
    comments = models.TextField()
    checked_by = models.ForeignKey(
        User, on_delete=models.RESTRICT
    )

# solution to update field in Emission model from stack overflow:
# https://stackoverflow.com/questions/71477386/update-a-model-field-when-another-modal-field-is-updated
    def save(self, *args, **kwargs):
        super().save(args, kwargs)
        Emission.objects.update(last_checked=self.date_checked)


# selection of user group on registration, solution from Stack Overflow:
# https://stackoverflow.com/questions/48544176/how-to-set-default-group-for-new-user-in-django
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        instance.groups.add(Group.objects.get(name='emission_user'))
