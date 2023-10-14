from django.db import models
import json


class Office(models.Model):
    coordinates = models.JSONField()
    balloonContentHeader = models.CharField(max_length=255)
    balloonContentBody = models.TextField()
    balloonContentFooter = models.CharField(max_length=255)
    iconImageHref = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # Разделить строку координат на два числа
        latitude, longitude = map(float, self.coordinates.split(','))
        # Преобразовать координаты в формат JSON
        self.coordinates = json.dumps([latitude, longitude])
        super(Office, self).save(*args, **kwargs)
