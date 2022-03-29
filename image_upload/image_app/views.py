
# Create your views here.
import os
from bdb import set_trace
from textwrap import fill
from tkinter.filedialog import SaveAs
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import HotelForm, ogImage
from PIL import Image, ImageOps

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

def photo_editor(request, image_id, image_style=None):
	image_data = ogImage.objects.get(pk=image_id)
	initial_path = image_data.image.path
	image = image_data.image
	name = image_data.name
	# if image_path != 'mod.png':
		
	# 	img = Image.open('../image_upload' + image_path.removesuffix('/grayscale'))
	# 	img.save('mod.png')

	# 	print(image_path)
		
	if image_style == 'grayscale':
		gs_image = Image.open(f"../image_upload/media/{image}").convert('L')
		

		image_data.image.name = f'/images/grayscale{image_id}.png'
		new_path = settings.MEDIA_ROOT + image_data.image.name
		print('new_path = ' + new_path)
		os.rename(initial_path, new_path)
		image_data.save()
		gs_image.save(f"../image_upload/media/images/grayscale{image_id}.png")
		
		# import pdb; pdb.set_trace()
		#maybe return to photo_editor/1/ not ../image_style
		image = image_data.image

	if image_style == 'posterize':
		print('something happend')
	# 	answer = simpledialog.askinteger("Input", "What color do you want?", minvalue=1, maxvalue=8)

	# 	# creating a image1 object 
	# 	im1 = Image.open("mod.png") 

	# 	# applying posterize method 
	# 	im2 = ImageOps.posterize(im1, answer)

	
	context = {'image' : image, 'name' : name}

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

