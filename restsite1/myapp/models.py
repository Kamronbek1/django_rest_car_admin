from django.contrib.auth.models import User
from django.db import models

from django.conf import settings
from tinymce.models import HTMLField


class Driver(models.Model):
    for iso, lang in settings.LANGUAGES:
        locals()[f"firstname_{iso}"] = models.CharField(max_length=50, blank=True, null=True)
        locals()[f"lastname_{iso}"] = models.CharField(max_length=50, blank=True, null=True)
    createdBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="drivers_created_by")
    updatedBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="drivers_updated_by")
    birthdate = models.DateField()
    bio = HTMLField(max_length=5000, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=15)
    salary = models.IntegerField()

    def __str__(self):
        # for iso, _ in settings.LANGUAGES:
        #     getattr()
        return str(self.id)


class Car(models.Model):
    for iso, _ in settings.LANGUAGES:
        locals()[f"name_{iso}"] = models.CharField(max_length=255)
        locals()[f"color_{iso}"] = models.CharField(max_length=50)
        if iso == 'ru':
            locals()[f"image_{iso}"] = models.ImageField(upload_to=f"car_images/{iso}/")
        else:
            locals()[f"image_{iso}"] = models.ImageField(upload_to=f"car_images/{iso}/", null=True, blank=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='cars')
    createdBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="cars_created_by")
    updatedBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="cars_updated_by")
    car_number = models.CharField(max_length=50, default='00x000yy ab')
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
