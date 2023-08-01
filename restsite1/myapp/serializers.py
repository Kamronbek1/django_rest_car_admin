from collections import OrderedDict

from django.conf import settings
from rest_framework import serializers

# from modeltranslation
from .models import Car, Driver
from django.utils import translation


class I18nModelSerializer(serializers.ModelSerializer):

    # def get_field_names(self, declared_fields, info):
    #     # model = self.Meta.model._meta.get_field('image_ru').get_internal_type()
    #     model = self.Meta.model._meta.get_fields()
    #     # print(type(model))
    #     print((model))
    #     # for k in model:
    #     #     print(k, ' ', k)
    #     fields = super().get_field_names(declared_fields, info)
    #     lang = translation.get_language()
    #     if lang:
    #         i18n_fields = getattr(self.Meta, 'i18n_fields', None)
    #         # i18n_images = getattr(self.Meta, 'i18n_images', None)
    #         # print('fields ', i18n_fields)
    #         result = []
    #
    #         for k in i18n_fields[1]:
    #             result.append("{}_{}".format(k, lang))
    #         for f in fields:
    #             result.append(f)
    #         # if i18n_images is not None:
    #         #     for f in i18n_images:
    #         #         for iso, _ in settings.LANGUAGES:
    #         #             result.append("{}_{}".format(f, iso))
    #     else:
    #         result = fields
    #     print(result)
    #     return result

    def to_representation(self, instance):
        i18n_fields = getattr(self.Meta, 'i18n_fields', None)
        fields_lang = [f"{field}_{key}" for field in i18n_fields[1] for key, _ in settings.LANGUAGES]
        representation = super().to_representation(instance)
        if i18n_fields[0] == 'catch':
            for k in i18n_fields[1]:
                representation[f'{k}'] = representation.pop("{}_{}".format(k, translation.get_language()))
                if not getattr(instance, "{}_{}".format(k, translation.get_language()), None):
                    for iso, _ in settings.LANGUAGES:
                        if getattr(instance, f'{k}_{iso}', None):
                            representation[f'{k}'] = representation.pop("{}_{}".format(k, iso))
                            break
                        else:
                            continue
                if not representation[k]:
                    representation[k] = None

            return {key: value for key, value in representation.items() if key not in fields_lang}


class CarSerializer(I18nModelSerializer):
    class Meta:
        model = Car
        i18n_fields = ("catch", ('name', 'color', 'image'))
        fields = "__all__"
        extra_kwargs = {
            "createdBy": {
                'read_only': True,
            },
            "updatedBy": {
                'read_only': True,
            },
            "image_ru": {
                'required': True
            }
        }


class DriverSerializer(I18nModelSerializer):
    cars = CarSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Driver
        i18n_fields = ('lastname', 'firstname',)
        fields = 'id', 'birthdate', 'phone', 'salary', 'time_create', 'cars', 'createdBy', 'updatedBy',
        extra_kwargs = {
            "createdBy": {
                'read_only': True,
            },
            "updatedBy": {
                'read_only': True,
            },
            # "cars": {
            #     'read_only': False,
            # },
        }
