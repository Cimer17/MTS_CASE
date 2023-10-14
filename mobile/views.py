from django.shortcuts import render
from .models import *
import json


def get_data():
    offices = Office.objects.all()
    data = {
        "type": "FeatureCollection",
        "features": []
    }
    for office in offices:
        feature = {
            "type": "Feature",
            "id": office.id,  # Включаем поле id
            "geometry": {
                "type": "Point",
                "coordinates": office.coordinates
            },
            "properties": {
                "balloonContentHeader": office.balloonContentHeader,
                "balloonContentBody": office.balloonContentBody,
                "balloonContentFooter": office.balloonContentFooter,
                "iconImageHref": office.iconImageHref
            }
        }
        data["features"].append(feature)
    with open('static/data.json', 'w', encoding='UTF-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def index(request):
    return render(request, 'mobile/index.html')


def my_ofice(request):
    return render(request, 'mobile/myoffice.html')


def maps(request):
    data = get_data()
    return render(request, 'mobile/maps.html')


def profile(request):
    return render(request, 'mobile/profile.html')


def chat(request):
    return render(request, 'mobile/chat.html')
