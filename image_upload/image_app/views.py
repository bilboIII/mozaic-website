
# Create your views here.
from ast import Return
from bdb import set_trace
from textwrap import fill
from tkinter.filedialog import SaveAs
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import HotelForm, ogImage
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
	mysuperdupreform = HotelForm()
	#takes "ogImage" function form models.py and saves it as images
	images = ogImage.objects.all()
	#not quite sure yet
	return render(request, template_name='hotel_image_form.html', context={'form' : mysuperdupreform, 'images' : images})

def photo_editor(request, image_name, image_path, image_style=None):
	
	if image_path != 'mod.png':
		
		img = Image.open('../image_upload' + image_path.removesuffix('/grayscale'))
		img.save('mod.png')
		
	if image_style == 'grayscale/?':
		gs_image = Image.open('mod.png').convert('L')
	
		gs_image.save('mod.png')
		import pdb; pdb.set_trace()
		image_path = 'mod.png'
	
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

