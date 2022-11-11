from rest_framework import serializers
from .models import *


class Permission_Serializer(serializers.ModelSerializer):

    class Meta:
        depth = 1
        model = PermissionModel
        fields = ('user', 'register_user', 'modify_permission', 'dashboard', 'company', 'inward_form', 'vehicle_entry', 'mother_table', 'slitted_table', 'pipe_inward', 'planning', 'coil_planning', 'slitt_plan', 'pc_pipe', 'download',
                  'create_company', 'company_table', 'inward', 'polish_plan', 'coil_plan', 'pipe_planning', 'slitting', 'pipe', 'first_obse', 'inprocess', 'tubemill', 'tubemill_movement', 'polish_inspection', 'polish_movement', 'dispatch', 'coil_dispatch', 'scrap_data', 'pipe_sales', 'coil_sales',
                  'sales_scrap', 'data_process', 'entry_vehicle', 'process_inward', 'production', 'slitting_process', 'failed_challan', 'process_dispatch', 'process_booking', 'process_sales_dispatch', 'sales', 'company_list', 'booking_sales', 'order', 'coil_order', 'warehouse', 'mothercoil', 'slittedcoil', 'scrap', 'challan')
