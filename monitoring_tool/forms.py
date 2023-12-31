from .models import Emission, EmissionCheck
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class EmissionSubmissionForm(forms.ModelForm):

    class Meta:
        model = Emission
        fields = ('title', 'location', 'emission_image',
                  'description', 'latitude', 'longitude',
                  'type')
# solution for selecting form fields as date type and
# for text area rows from stack overflow:
# https://stackoverflow.com/que`stions/22846048/django-form-as-p-datefield-not-showing-input-type-as-date
# https://stackoverflow.com/questions/6536373/how-can-i-set-the-size-of-rows-columns-in-textfield-in-django-models
        widgets = {
            'title':
            forms.TextInput(
                attrs={'placeholder': 'Please enter a title max 15 characters'}
                ),
            'location':
            forms.TextInput(attrs={'placeholder': 'Please enter a location '
                                                  'i.e module, block or '
                                                  'building'}),
            'description':
            forms.Textarea(attrs={'rows': 3, 'cols': 40,
                                  'placeholder': "Please enter "
                                  "a short description of the "
                                  "emission max 100 characters.",
                                  "required": True}),
            # set max and min values for latitude and longitude to prevent
            # erroneous entries in submission.
            'latitude':
            forms.NumberInput(attrs={'max': 90, 'min': -90}),
            'longitude':
            forms.NumberInput(attrs={'max': 180, 'min': -180}),
        }


class EmissionCloseOutForm(forms.ModelForm):
    class Meta:
        model = Emission
        fields = (
            'close_out_comments',
            )
        widgets = {
            'close_out_comments':
            forms.Textarea(attrs={'rows': 3, 'cols': 40,
                                  'placeholder': "Please enter "
                                  "a close out comment for the emission"
                                  " max 100 characters.",
                                  'required': True}),
        }


class CheckSubmissionForm(forms.ModelForm):

    class Meta:
        model = EmissionCheck
        fields = ('status', 'comments')
# solution for selecting form fields as date type and
# for text area rows from stack overflow:
# https://stackoverflow.com/que`stions/22846048/django-form-as-p-datefield-not-showing-input-type-as-date
# https://stackoverflow.com/questions/6536373/how-can-i-set-the-size-of-rows-columns-in-textfield-in-django-models
        widgets = {
            'comments':
            forms.Textarea(attrs={'rows': 3, 'cols': 40,
                                  'placeholder': "Please enter "
                                  "a short description of the "
                                  "check max 100 characters.",
                                  "required": True}),
        }


class CheckEditForm(forms.ModelForm):

    class Meta:
        model = EmissionCheck
        fields = ('comments', 'status', 'edit_comments')
# solution for selecting form fields as date type and
# for text area rows from stack overflow:
# https://stackoverflow.com/que`stions/22846048/django-form-as-p-datefield-not-showing-input-type-as-date
# https://stackoverflow.com/questions/6536373/how-can-i-set-the-size-of-rows-columns-in-textfield-in-django-models
        widgets = {
            'edit_comments':
            forms.Textarea(attrs={'rows': 3, 'cols': 40,
                                  'placeholder': "Please enter "
                                  "a reason for the edit"
                                  " max 100 characters.",
                                  'required': True, 'id': 'editComments'})
        }
