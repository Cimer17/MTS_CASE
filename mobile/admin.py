from django.contrib import admin
from django import forms
from .models import Office

class CoordinatesInput(forms.TextInput):
    def value_from_datadict(self, data, files, name):
        value = data.get(name, None)
        if value:
            try:
                return [float(coord.strip()) for coord in value.split(',')]
            except (ValueError, TypeError):
                pass
        return None

class CoordinatesField(forms.CharField):
    def formfield(self, **kwargs):
        kwargs['widget'] = CoordinatesInput
        return super().formfield(**kwargs)

class OfficeAdminForm(forms.ModelForm):
    coordinates = CoordinatesField(required=False)

    class Meta:
        model = Office
        fields = '__all__'

class OfficeAdmin(admin.ModelAdmin):
    form = OfficeAdminForm
    list_display = ('id', '__str__') 
    list_display_links = ('id', '__str__')
    fieldsets = [
        (None, {'fields': ('coordinates', 'balloonContentHeader', 'balloonContentBody', 'balloonContentFooter')}),
    ]

admin.site.register(Office, OfficeAdmin)
