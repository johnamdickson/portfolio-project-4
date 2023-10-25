from .models import Emission
from django import forms


class EmissionSubmission(forms.ModelForm):
    class Meta:
        model = Emission
        fields = ('title', 'location', 'emission_image', 
                  'description', 'latitude', 'longitude',
                  'next_check_due', 'current_check_due',
                  'status', 'type')
