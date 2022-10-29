from tabnanny import verbose
from django.contrib import admin
from manager.models import PermissionModel

# Register your models here.

class AccountInline(admin.StackedInline):
    model = PermissionModel
    verbose_name_plural = 'Manager'

admin.site.register(PermissionModel)