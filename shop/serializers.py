from rest_framework import serializers
from . models import Customer
from django.contrib.auth.models import User

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'
#('full_name', 'phone_number', 'email', 'store_name', 'address_line1', 'address_line2', 'pin_code','district','state','pan_number','gst_number')
#instead use __all__

    def update(self, instance, validated_data):
        instance.full_name = validated_data.get("full_name", instance.full_name)
        instance.phone_number = validated_data.get("phone_number", instance.phone_number)
        instance.save()
        return instance