from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import requests
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

def capabilitiesOnOff(token: str, device_id: str, turn: bool):
    url = r'https://api.iot.yandex.net/v1.0/devices/actions'
    headers = {'Authorization': 'Bearer' + ' ' + token}
    data = {'devices': [{'id': device_id, 'actions': [
        {'type':  'devices.capabilities.on_off', 'state': {'instance':  'on', 'value': turn}}]}]}
    return requests.post(url=url, headers=headers, data=json.dumps(data)).content


def lamp(turn):
    if turn:
        for i in range(len(device_ids)):
            capabilitiesOnOff(token, device_ids[i], True)
    else:
        for i in range(len(device_ids)):
            capabilitiesOnOff(token, device_ids[i], False)


def toggle_humidifier(request):
    print('yes')
    if request.method == 'POST':
        data = json.loads(request.body)
        isChecked = data.get("isChecked")
        if isChecked:
            capabilitiesOnOff(token, puzatic, True)
            message = "Увлажнитель включен"
        else:
            capabilitiesOnOff(token, puzatic, False)
            message = "Увлажнитель выключен"
        return JsonResponse({"message": message})
    return JsonResponse({"error": "Invalid request method"}, status=400)


def toggle_lamp(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        isChecked = data.get("isChecked")
        if isChecked:
            lamp(True)
            message = "Лампочка включена"
        else:
            lamp(False)
            message = "Лампочка выключена"
        return JsonResponse({"message": message})
    return JsonResponse({"error": "Invalid request method"}, status=400)
