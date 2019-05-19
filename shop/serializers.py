from rest_framework import serializers
from . models import Customer

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'
#('full_name', 'phone_number', 'email', 'store_name', 'address_line1', 'address_line2', 'pin_code','district','state','pan_number','gst_number')
#instead use __all__

class CustomerSerializerput(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('full_name', 'Phone_number')
