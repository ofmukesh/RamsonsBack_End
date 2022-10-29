import imp
from pyexpat import model
from django.contrib import admin
from .models import Test

# Register your models here.
@admin.register(Test)
class AdminClass(admin.ModelAdmin):
    list_display=['test']