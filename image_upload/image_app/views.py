
# Create your views here.
from ast import Return
from re import A
from tkinter.filedialog import SaveAs
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import *
from PIL import Image

# Create your views here.
def hotel_image_view(request):


	if request.method == 'POST':
		#calls "HotelForm" class form forms.ply 
		form = HotelForm(request.POST, request.FILES)

		#checks to see if an image was uploaded succesfully and saves it
		if form.is_valid():
			form.save()
		#sends you back to main page ("image_upload")
		return redirect("image_upload")
	#calls "HotelForm" class form forms.ply 
	form = HotelForm()
	#takes "ogImage" function form models.py and saves it as images
	images = ogImage.objects.all()
	#not quite sure yet
	return render(request, template_name='hotel_image_form.html', context={'form' : form, 'images' : images})

def photo_editor(request, image_name, image_path):
	
	context = {'image_name': image_name, 'image_path' : image_path}

	return render(request, 'photo_editor.html', context)

def grayscale(request, image_name, image_path):
	gs_image = Image.open('mod.png').convert('L')
	
	#enables colorize button (might look into way of implementing button )
	#self.color_button['state'] = 'normal'

	#updates the imgage
	gs_image.save('photo_edits/mod.png')
	context = {'image_name': image_name, 'image_path' : image_path}

	return render(request, 'photo_editor.html', context)

# def success(request):
# 	return HttpResponse('successfully uploaded')

