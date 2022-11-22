from rest_framework import serializers
from .models import company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = company
        fields = ('id', 'created_on', 'update_on', 'company_code', 'person_name', 'company_name',
                  'gst_no', 'emailid', 'phone_no', 'alternate_no', 'address', 'city', 'state', 'pincode', 'created_by', 'updated_by', 'active')

