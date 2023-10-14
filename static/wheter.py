from PIL import Image, ImageDraw, ImageFont
import requests

# Ваш API ключ OpenWeatherMap
api_key = 'f4910382bc2cdfed1954592a8e018b96'

picture_weather = {
    'ясно': ['weather/sun.png', 'Солнечно'],
    'пасмурно': ['weather/pas.png', 'Облачно'],
    'дождь': ['weather/rain.png', 'Дождь'],
    'ливень': ['weather/fastrain.png', 'Ливень'],
}

# Город, для которого вы хотите получить информацию о погоде
city = 'Kovrov'

# Формируем URL запроса
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=ru'

# Отправляем GET-запрос
response = requests.get(url)

# Проверяем успешность запроса
if response.status_code == 200:
    data = response.json()
    # Извлекаем информацию о температуре и состоянии погоды
    temperature = data['main']['temp'] - 273.15  # Конвертируем в градусы Цельсия
    weather = data['weather'][0]['description']
    try:
        # Открываем изображение baner_weather.png
        baner_image = Image.open('baner_weather.png')
        
        # Открываем изображение погоды
        weather_image = Image.open(picture_weather[weather][0])
        
        # Получаем ширину и высоту baner_image
        width, height = baner_image.size
        
        # Размещаем изображение погоды в верхнем левом углу baner_image
        baner_image.paste(weather_image, (0, 0), weather_image)
        
        # Создаем объект для рисования
        draw = ImageDraw.Draw(baner_image)
        
        # Загружаем шрифт
        font = ImageFont.load_default()
        
        # Рисуем надпись
        draw.text((10, height - 40), picture_weather[weather][1], fill='white', font=font)
        
        # Сохраняем измененное изображение
        baner_image.save('baner_weather_test.png')
        
        print(f'Температура в {city}: {temperature:.2f}°C')
        print(f'Состояние погоды: {picture_weather[weather][0]}')
    except:
        print(f'Температура в {city}: {temperature:.2f}°C')
        print(f'Состояние погоды: {picture_weather["ясно"][0]}')
else:
    print('Ошибка при запросе информации о погоде.')
