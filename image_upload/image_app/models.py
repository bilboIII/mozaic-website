from django.db import models

# Create your models here.
class ogImage(models.Model):
	image_id = models.IntegerField(primary_key=True)
	# creats input for "name" of image (not file name)
	name = models.CharField(max_length=50)
	#creats input for get the "image" and sows where is save it
	image = models.ImageField(upload_to='images/')
