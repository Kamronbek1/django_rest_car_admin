from django.contrib import admin
from django.utils import translation
from django.utils.safestring import mark_safe

from .models import Car, Driver

#
admin.site.site_header = 'My Custom Index Title'


class CarInline(admin.TabularInline):
    model = Car
    extra = 1
    readonly_fields = ['id', 'createdBy', 'updatedBy', 'time_create']


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = "__str__", 'id', 'birthdate', 'phone', 'salary', 'createdBy', 'updatedBy', 'time_create',
    inlines = [CarInline]
    readonly_fields = ['id', 'createdBy', 'updatedBy', 'time_create']

    def save_model(self, request, obj, form, change):
        if not change:
            obj.createdBy = request.user
        else:
            obj.updatedBy = request.user
        obj.save()

    def save_formset(self, request, form, formset, change):
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                if not instance.pk:
                    instance.createdBy = request.user
                    print('new ', instance)
                else:
                    instance.updatedBy = request.user
                instance.save()
            formset.save_m2m()


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    lang = translation.get_language()

    list_display = 'id', 'driver', f'color_{lang}', f'name_{lang}', 'image_tag', 'car_number', \
        'createdBy', 'updatedBy', 'time_create'
    readonly_fields = ['id', 'createdBy', 'updatedBy', 'time_create', 'image_tag']

    # fields = 'id', 'driver', 'car_number', 'createdBy', 'updatedBy',
    def image_tag(self, obj):
        print(obj)
        if obj.image_ru:
            return mark_safe(f'<img src="{obj.image_ru.url}" title="{obj.image_ru.name}" width="150" height="150" />')

    image_tag.short_description = 'Image'

    def save_model(self, request, obj, form, change):
        if not change:
            obj.createdBy = request.user
        else:
            obj.updatedBy = request.user
        obj.save()
