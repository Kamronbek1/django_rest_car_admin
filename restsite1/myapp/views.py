#  Copyright (c) 2023.

from rest_framework import viewsets, serializers

from .models import Car, Driver
from .permissions import HasGroupPermission
from .serializers import CarSerializer, DriverSerializer


#
# class CarViewSet(viewsets.ModelViewSet):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer


class CarAPIViewSet(viewsets.ModelViewSet):
    # renderer_classes = JSONRenderer,
    serializer_class = CarSerializer
    permission_classes = [HasGroupPermission]
    required_groups = {
        'GET': ['user_group', 'manager'],
        'POST': ['manager'],
        'PUT': ['manager'],
        'DELETE': ['manager'],
    }

    createdBy = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    updatedBy = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    def get_queryset(self):
        return Car.objects.all()

    def perform_create(self, serializer):
        serializer.save(createdBy=self.request.user)


class DriverAPIViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    permission_classes = (HasGroupPermission,)
    required_groups = {
        'GET': ['user_group', 'manager'],
        'POST': ['manager'],
        'PUT': ['manager'],
        'DELETE': ['manager'],
    }
    createdBy = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    updatedBy = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    def perform_create(self, serializer):
        serializer.save(createdBy=self.request.user)

# class MyCarCRUDAPIView(APIView):
#     def post(self, request):
#         from django.http import JsonResponse
#         # return response.Response({'json': "sdsdf"})
#         return JsonResponse({'json': "sdsdf"})
#
#     def get(self, request):
#         from django.http import JsonResponse
#         # return response.Response({'json': "sdsdf"})
#         return JsonResponse({'json': "sdsdf"})
#
#
# class BrotherCarCRUDAPIView(APIView):
#     def post(self, request):
#         from django.http import JsonResponse
#         # return response.Response({'json': "sdsdf"})
#         driver = Driver.objects.create(
#
#         )
#
#         return JsonResponse(DriverSerializer(driver).data)
#
#     def get(self, request):
#         from django.http import JsonResponse
#         # return response.Response({'json': "sdsdf"})
#         return JsonResponse({'json': "sdsdf"})
