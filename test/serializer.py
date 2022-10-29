from rest_framework import serializers
from .models import Test
from django.db import transaction

class TestSeria(serializers.ModelSerializer):
    def create(self,validated_data):
        print("inst",validated_data)
        with transaction.atomic():
            return validated_data
    class Meta:
        model=Test
        fields = '__all__'

    