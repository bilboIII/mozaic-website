# forms.py
from django import forms
from .models import *
from django.forms import TextInput

class UploadForm(forms.ModelForm):

	class Meta:
		#takes "ogImage" function from models.py and names it model
		model = ogImage
		#takes "name" and "image" and puts ie in a list called "fields"
		fields = ['name', 'image']

		widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name for image'
                }),
        }
