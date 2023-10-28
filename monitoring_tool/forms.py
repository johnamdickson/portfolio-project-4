from .models import Emission
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class EmissionSubmissionForm(forms.ModelForm):
    class Meta:
        model = Emission
        fields = ('title', 'location', 'emission_image',
                  'description', 'latitude', 'longitude',
                  'next_check_due', 'current_check_due',
                  'type')
# solution for selecting form fields as date type and for text area rows from stack overflow:
# https://stackoverflow.com/questions/22846048/django-form-as-p-datefield-not-showing-input-type-as-date
# https://stackoverflow.com/questions/6536373/how-can-i-set-the-size-of-rows-columns-in-textfield-in-django-models
        widgets = {
            'next_check_due': DateInput(),
            'current_check_due': DateInput(),
            'description': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
        }
