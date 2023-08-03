#  Copyright (c) 2023.
from django.conf import settings
from rest_framework import viewsets, serializers
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
from .models import Car, Driver
from .permissions import HasGroupPermission, IsSuperUser
from .serializers import CarSerializer, DriverSerializer


#
# class CarViewSet(viewsets.ModelViewSet):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer


class CarAPIViewSet(viewsets.ModelViewSet):
    # renderer_classes = JSONRenderer,
    serializer_class = CarSerializer
    permission_classes = [HasGroupPermission, IsSuperUser]
    required_groups = {
        'GET': ['user_group', 'manager'],
        'POST': ['manager'],
        'PUT': ['manager'],
        'PATCH': ['manager'],
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
    permission_classes = (HasGroupPermission, IsSuperUser)
    required_groups = {
        'GET': ['user_group', 'manager'],
        'POST': ['manager'],
        'PUT': ['manager'],
        'PATCH': ['manager'],
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

    def get_queryset(self):
        return Driver.objects.all()


@csrf_exempt
def image_upload(request):
    if request.method == 'POST':
        print('tinymce image_upload method called!')
        file = request.FILES['file']  # get the uploaded file
        file_name = file.name
        # save the file to your desired location
        save_path = os.path.join(settings.MEDIA_ROOT, 'uploads', file_name)
        print(save_path)
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        # return a JSON response with the URL of the image
        return JsonResponse({'location': os.path.join(settings.MEDIA_URL, 'uploads', file_name)})

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
