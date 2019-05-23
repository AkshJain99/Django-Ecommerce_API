from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomerSerializer
from .models import Customer
from rest_framework import generics
from .decorators import validate_request_data

class CustomerList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request, *args, **kwargs):
        try:
            customer1 = self.queryset.get(pk=kwargs["pk"])
            return Response(CustomerSerializer(customer1).data)
        except Customer.DoesNotExist:
            return Response(
                data={
                    "message": "Customer with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
)

    @validate_request_data
    def put(self, request, *args, **kwargs):
        try:
            customer1 = self.queryset.get(pk=kwargs["pk"])
            serializer = CustomerSerializer()
            update_details = serializer.update(customer1, request.data)
            return Response(CustomerSerializer(update_details).data)
        except Customer.DoesNotExist:
            return Response(
                data={
                    "message":"Customer with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND

            )


        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)