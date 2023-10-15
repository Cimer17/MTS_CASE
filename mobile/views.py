from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import requests
import json
from django.views.decorators.csrf import csrf_exempt


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


token = 'y0_AgAAAAAfsIQlAAqWqQAAAADuJBIHD18WPQVEQ6ukgX7hUslf9fRkgVs'
device_ids = ['045ab865-070d-4a99-994f-78cb17de2abd',
              'e4fd0567-d1d7-4064-9597-df391234cbac']


def TurnOnOffLamp(token, device_id, turn):
    url = r'https://api.iot.yandex.net/v1.0/devices/actions'
    headers = {'Authorization': 'Bearer' + ' ' + token}
    data = {'devices': [{'id': device_id, 'actions': [{'type': 'devices.capabilities.on_off', 'state': {
        'instance': 'on', 'value': turn}} for device_id in device_ids]}]}
    return requests.post(url=url, headers=headers, data=json.dumps(data)).content


def lamp(turn):
    for device_id in device_ids:
        TurnOnOffLamp(token, device_id, turn)


@csrf_exempt
def toggle_lamp(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        isChecked = data.get("isChecked")
        if isChecked:
            lamp(False)
            message = "Лампочка включена"
        else:
            lamp(True)
            message = "Лампочка выключена"
        return JsonResponse({"message": message})
    return JsonResponse({"error": "Invalid request method"}, status=400)  # Вернуть JSON-ответ для GET-запроса
