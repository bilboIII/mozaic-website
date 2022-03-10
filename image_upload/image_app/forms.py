# forms.py
from django import forms
from .models import *

class HotelForm(forms.ModelForm):

	class Meta:
		#takes "ogImage" function from models.py and names it model
		model = ogImage
		#takes "name" and "image" and puts ie in a list called "fields"
		fields = ['name', 'image']
