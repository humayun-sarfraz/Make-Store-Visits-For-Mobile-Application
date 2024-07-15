from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee, Store, Visit
from .serializers import StoreSerializer, VisitSerializer
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

class PhoneAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            raise AuthenticationFailed('No authorization header provided')
        
        try:
            auth_type, phone_number = auth_header.split()
            if auth_type != 'Phone':
                raise AuthenticationFailed('Invalid auth type')
            employee = Employee.objects.get(phone_number=phone_number)
            return (employee, None)
        except Employee.DoesNotExist:
            raise AuthenticationFailed('Employee not found')
        except ValueError:
            raise AuthenticationFailed('Invalid authorization header')

class StoreListView(APIView):
    authentication_classes = [PhoneAuthentication]

    def get(self, request):
        employee = request.user
        stores = Store.objects.filter(employee=employee)
        if not stores.exists():
            return Response({'error': 'No stores found for this employee'}, status=status.HTTP_404_NOT_FOUND)
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)

class VisitCreateView(APIView):
    authentication_classes = [PhoneAuthentication]

    def post(self, request):
        employee = request.user
        store_pk = request.data.get('store_pk')
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')

        try:
            store = Store.objects.get(pk=store_pk, employee=employee)
        except Store.DoesNotExist:
            return Response({'error': 'Store not found for this employee'}, status=status.HTTP_404_NOT_FOUND)

        visit = Visit.objects.create(store=store, employee=employee, latitude=latitude, longitude=longitude)
        serializer = VisitSerializer(visit)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
