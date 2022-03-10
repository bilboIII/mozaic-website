from django.contrib import admin

# Register your models here.
from .models import ogImage

#basic backend way to ad photo to program via admin
admin.site.register(ogImage)