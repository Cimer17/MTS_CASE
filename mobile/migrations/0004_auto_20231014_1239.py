# Generated by Django 3.2 on 2023-10-14 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0003_alter_office_coordinates'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='office',
            options={'verbose_name': 'Офис', 'verbose_name_plural': 'Офисы'},
        ),
        migrations.AlterField(
            model_name='office',
            name='balloonContentBody',
            field=models.TextField(verbose_name='Содержание балуна'),
        ),
        migrations.AlterField(
            model_name='office',
            name='balloonContentFooter',
            field=models.CharField(max_length=255, verbose_name='Футер балуна'),
        ),
        migrations.AlterField(
            model_name='office',
            name='balloonContentHeader',
            field=models.CharField(max_length=255, verbose_name='Заголовок балуна'),
        ),
        migrations.AlterField(
            model_name='office',
            name='coordinates',
            field=models.JSONField(help_text='Введите координаты в формате [широта, долгота]', verbose_name='Координаты'),
        ),
        migrations.AlterField(
            model_name='office',
            name='iconImageHref',
            field=models.CharField(default='static/maps/metka.png', max_length=255),
        ),
    ]
