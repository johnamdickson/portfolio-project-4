from django.db import models
from django.contrib.auth.models import User, Group
import constants as k
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField


class Emission(models.Model):
    choices = k.EMISSION_TYPES
    title = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=50, unique=False)
    slug = models.SlugField(max_length=200, unique=True)
    username = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="monitoring_tool_emissions"
    )
    emission_image = CloudinaryField('image', default='placeholder')
    description = models.TextField(blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_checked = models.DateField(auto_now=True)
    next_check_due = models.DateField(auto_now=False)
    current_check_due = models.DateField(auto_now=False)
    status = models.IntegerField(choices=k.STATUS, default=0)
    type = models.IntegerField(choices=choices, default=0)

# solution to accessing strings values from choices tuple:
# https://stackoverflow.com/questions/60556709/how-do-i-get-the-string-value-of-the-tuple-in-django
    def get_emission_type(self):
        return dict(self.choices).get(self.type)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def calculate_check_complete(self):
        if self.current_check_due <= self.last_checked <= self.next_check_due:
            return "Checks Complete"
        else:
            return "Checks Outstanding"


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