from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Approved"))


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
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    next_check_due = models.DateField(auto_now=False)
    current_check_due = models.DateField(auto_now=False)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


class EmissionCheck(models.Model):
    emission = models.ForeignKey(Emission, on_delete=models.CASCADE,
                                 related_name="emissioncheck")
    title = models.CharField(max_length=30, unique=True)
    date_checked = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=30, unique=False)
    comments = models.TextField()
    checked_by = models.CharField(max_length=50)
