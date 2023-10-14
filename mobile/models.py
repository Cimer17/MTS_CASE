from django.db import models
import json



class Office(models.Model):
    coordinates = models.JSONField(verbose_name="Координаты", help_text="Введите координаты в формате [широта, долгота]",)
    balloonContentHeader = models.CharField(verbose_name="Заголовок балуна", max_length=255)
    balloonContentBody = models.TextField(verbose_name="Содержание балуна")
    balloonContentFooter = models.CharField(max_length=255, verbose_name="Футер балуна")
    iconImageHref = models.CharField(max_length=255, default="static/maps/metka.png")
    
    def save(self, *args, **kwargs):
        # Проверяем, если координаты - это строка, преобразуем их в список
        if isinstance(self.coordinates, str):
            try:
                self.coordinates = [float(coord.strip()) for coord in self.coordinates.split(',')]
            except (ValueError, TypeError):
                pass
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Офис'
        verbose_name_plural = 'Офисы'

