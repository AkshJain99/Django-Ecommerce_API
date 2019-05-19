from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomerSerializer
from .models import Customer


class CustomerList(APIView):

    def get(self, request):
        customer1 = Customer.objects.all()
        serializer = CustomerSerializer(customer1, many= True)
        return Response(serializer.data)

    def put(self, request):
        customer1 = Customer.objects.all()
        serializer = CustomerSerializer(customer1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)