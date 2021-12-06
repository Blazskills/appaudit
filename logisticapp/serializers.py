from django.db.models import fields
from rest_framework import serializers
from .models import RequestHeader


class LogisticExpensesSerializer(serializers.ModelSerializer):
    requestheader_name = serializers.CharField(
        max_length=255, min_length=10)
    # product_quantity = serializers.IntegerField(required=False, default=1)

    class Meta:
        model = RequestHeader
        fields = ['requestheader_id', 'request_header_creator',
                  'requestheader_name', 'department_header_onwer']


    
    
    
    def create(self, validated_data):
        return RequestHeader.objects.create(**validated_data)

