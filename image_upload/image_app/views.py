# Create your views here.
from wsgiref.util import FileWrapper
import os
from bdb import set_trace
from textwrap import fill
from tkinter.filedialog import SaveAs
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import UploadForm, ogImage
from PIL import Image, ImageOps
import mimetypes


# Create your views here.
def image_view(request):

	if request.method == 'POST':
		#calls "UploadForm" class form forms.ply 
		form = UploadForm(request.POST, request.FILES)

		#checks to see if an image was uploaded succesfully and saves it
		if form.is_valid():
			form.save()
		#sends you back to main page ("image_upload")
		return redirect("image_upload")
	#calls "UploadForm" class form forms.ply 
	mysuperdupreform = UploadForm()
	#takes "ogImage" function form models.py and saves it as images
	images = ogImage.objects.all()
	#not quite sure yet
	return render(request, template_name='image_form.html', context={'form' : mysuperdupreform, 'images' : images})

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
		
		image_data.image.name = f'images/grayscale{image_id}.png'
		new_path = settings.MEDIA_ROOT + '\\' + image_data.image.name
		print('new_path = ' + new_path)
		os.rename(initial_path, new_path)
		image_data.save()
		gs_image.save(f"../image_upload/media/images/grayscale{image_id}.png")
		
		# import pdb; pdb.set_trace()
		#maybe return to photo_editor/1/ not ../image_style
		# image = image_data.image

	if image_style == 'posterize':
		answer = 3
		
		# creating a image1 object 
		im1 = Image.open(f"../image_upload/media/{image}") 
		# applying posterize method 
		im2 = ImageOps.posterize(im1, answer)

		image_data.image.name = f'images/posterize{image_id}.png'
		new_path = settings.MEDIA_ROOT + '\\' + image_data.image.name
		print('new_path = ' + new_path)
		os.rename(initial_path, new_path)
		image_data.save()

		im2.save(f"../image_upload/media/images/posterize{image_id}.png")
		
	if image_style == 'pixelate':
		answer = 3
		
		img = Image.open(f"../image_upload/media/{image}")
		w = 78
		h = 108
		imgSmall = img.resize((w, h), resample=Image.BILINEAR)
		pixel = imgSmall.resize(img.size,Image.NEAREST)

		image_data.image.name = f'images/pixelate{image_id}.png'
		new_path = settings.MEDIA_ROOT + '\\' + image_data.image.name
		print('new_path = ' + new_path)
		os.rename(initial_path, new_path)
		image_data.save()

		pixel.save(f"../image_upload/media/images/pixelate{image_id}.png")

	if image_style == 'colorize':
		colors = [(0, 0, 255), (255, 0, 0), (255, 153, 0), (255, 255, 0), (255, 255, 255)] #this shoud be the base colors, also idea the initialcolor for the colorchooser
		
		#get a list of the picture
		img = Image.open(f"../image_upload/media/{image}")
		img.convert("RGB")
		sequence_of_pixels = img.getdata()

		#take img and colorize it
		newPic = []

		for x in sequence_of_pixels:
			#blue the first color in 'colors' list
			if x in range(0, 91):
				color = colors[0]
				#red the second color in 'colors' list
			elif x in range(91, 121):
				color = colors[1]
				#orange the third color in 'colors' list
			elif x in range(121, 151):
				color = colors[2]
				#yellow the forth color in 'colors' list
			elif x in range(151, 180):
				color = colors[3]
				#white the fith color in 'colors' list
			else:
				color = colors[4]
			
			newPic.append(color)

		#creats new image and saves the new data to said image
		img1 = Image.new("RGB", (img.size), (255, 255, 255))

		img1.putdata(newPic)

		image_data.image.name = f'images/colorize{image_id}.png'
		new_path = settings.MEDIA_ROOT + '\\' + image_data.image.name
		print('new_path = ' + new_path)
		os.rename(initial_path, new_path)
		image_data.save()

		img1.save(f"../image_upload/media/images/colorize{image_id}.png")

	if image_style == 'grid':
		pass

	context = {'image_data' : image_data}

	return render(request, 'photo_editor.html', context)

def download_file(request, image_id):
    img = ogImage.objects.get(pk=image_id)
    wrapper      = FileWrapper(open(img.image.path))  # img.file returns full path to the image
    content_type = mimetypes.guess_type(filename)[0]  # Use mimetypes to get file type
    response     = HttpResponse(wrapper,content_type=content_type)  
    response['Content-Length']      = os.path.getsize(img.image.path)    
    response['Content-Disposition'] = "attachment; filename=%s" %  img.name
    return response

