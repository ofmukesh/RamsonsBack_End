from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class PermissionModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Main data
    admin = models.BooleanField(default=False, null=True)
    register_user = models.BooleanField(default=False, null=True)
    modify_permission = models.BooleanField(default=False, null=True)
    dashboard = models.BooleanField(null=True, default=False,)
    company = models.BooleanField('Company', null=True, default=False,)
    create_company = models.BooleanField(null=True, default=False,)
    company_table = models.BooleanField(null=True, default=False,)
    inward = models.BooleanField(null=True, default=False,)
    inward_form = models.BooleanField(null=True, default=False,)
    vehicle_entry = models.BooleanField(null=True, default=False,)
    mother_table = models.BooleanField(null=True, default=False,)
    slitted_table = models.BooleanField(null=True, default=False,)
    pipe_inward = models.BooleanField(null=True, default=False,)
    planning = models.BooleanField(null=True, default=False,)
    coil_planning = models.BooleanField(null=True, default=False,)
    slitt_plan = models.BooleanField(null=True, default=False,)
    polish_plan = models.BooleanField(null=True, default=False,)
    coil_plan = models.BooleanField(null=True, default=False,)
    pipe_planning = models.BooleanField(null=True, default=False,)
    slitting = models.BooleanField(null=True, default=False,)
    pipe = models.BooleanField(null=True, default=False,)
    first_obse = models.BooleanField(null=True, default=False,)
    inprocess = models.BooleanField(null=True, default=False,)
    tubemill = models.BooleanField(null=True, default=False,)
    tubemill_movement = models.BooleanField(null=True, default=False,)
    polish_inspection = models.BooleanField(null=True, default=False,)
    polish_movement = models.BooleanField(null=True, default=False,)
    dispatch = models.BooleanField(null=True, default=False,)
    coil_dispatch = models.BooleanField(null=True, default=False,)
    scrap_data = models.BooleanField(null=True, default=False,)
    pipe_sales = models.BooleanField(null=True, default=False,)
    coil_sales = models.BooleanField(null=True, default=False,)
    sales_scrap = models.BooleanField(null=True, default=False,)
    data_process = models.BooleanField(null=True, default=False,)
    entry_vehicle = models.BooleanField(null=True, default=False,)
    process_inward = models.BooleanField(null=True, default=False,)
    production = models.BooleanField(null=True, default=False,)
    slitting_process = models.BooleanField(null=True, default=False,)
    failed_challan = models.BooleanField(null=True, default=False,)
    process_dispatch = models.BooleanField(null=True, default=False,)
    process_booking = models.BooleanField(null=True, default=False,)
    process_sales_dispatch = models.BooleanField(null=True, default=False,)
    sales = models.BooleanField(null=True, default=False,)
    company_list = models.BooleanField(null=True, default=False,)
    booking_sales = models.BooleanField(null=True, default=False,)
    order = models.BooleanField(null=True, default=False,)
    coil_order = models.BooleanField(null=True, default=False,)
    warehouse = models.BooleanField(null=True, default=False,)
    mothercoil = models.BooleanField(null=True, default=False,)
    slittedcoil = models.BooleanField(null=True, default=False,)
    scrap = models.BooleanField(null=True, default=False,)
    challan = models.BooleanField(null=True, default=False,)
    pc_pipe = models.BooleanField(null=True, default=False,)
    download = models.BooleanField(null=True, default=False,)

    def __str__(self):
        return self.user.username
