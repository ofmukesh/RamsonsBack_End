from django.db import models


def companyCode():
    print("company code")
    prefix = "COM/"
    try:
        item = company.objects.latest('id')
        return prefix + str(item.id + 1).rjust(4, '0')
    except:
        return prefix + str(1).rjust(4, '0')


class company(models.Model):
    created_on = models.DateTimeField(auto_now=True)
    update_on = models.DateTimeField(auto_now_add=True)
    company_code = models.CharField(max_length=10, default=companyCode)
    person_name = models.CharField(max_length=50, blank=True)
    company_name = models.CharField(max_length=100, blank=True)
    gst_no = models.CharField(max_length=25, blank=True)
    emailid = models.CharField(max_length=100, blank=True)
    phone_no = models.CharField(max_length=10, blank=True)
    alternate_no = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    pincode = models.CharField(max_length=6, blank=True)
    created_by = models.ForeignKey("auth.User",
                                   verbose_name=("Created By"),
                                   related_name="company_created_by",
                                   on_delete=models.SET_NULL,
                                   blank=True,
                                   null=True)
    updated_by = models.ForeignKey("auth.User",
                                   verbose_name=("Updated By"),
                                   related_name="company_updated_by",
                                   on_delete=models.SET_NULL,
                                   blank=True,
                                   null=True)
    active = models.BooleanField("Active", default=True, null=True)

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name_plural = ("Companies")
