from django.urls import path
from . import views

urlpatterns = {
    path('photo_editor/', views.photo_editor, name='photo_editor'),
}