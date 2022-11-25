from rest_framework import viewsets
from .serializer import CompanySerializer
from .models import company
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import F


class ComapnyView(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = company.objects.filter(active=True).order_by('-update_on')
    filterset_fields = {'company_name': [
        "in"], 'person_name': ['contains'], 'phone_no': ['contains'], 'created_on': ['range']}

    @action(detail=False)
    def names(self, request):
        queryset = company.objects.values(
            value=F('id'), label=F('company_name'))
        return Response(queryset)
