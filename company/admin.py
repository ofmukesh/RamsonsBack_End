from django.contrib import admin
from .models import company
# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_on', 'update_on', 'company_id', 'person_name', 'company_name',
                    'gst_no', 'emailid', 'phone_no', 'alternate_no', 'address', 'city', 'state', 'pincode', 'created_by', 'updated_by', 'active')


admin.site.register(company,CompanyAdmin)
