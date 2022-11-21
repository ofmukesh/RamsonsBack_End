from rest_framework import viewsets
from .serializer import CompanySerializer
from .models import company


class ComapnyView(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = company.objects.order_by('-update_on')
    filterset_fields = {'company_name': [
        "in"], 'person_name': ['contains'],'phone_no':['contains'],'created_on':['range']}
