import requests
from datetime import datetime
from datetime import timezone


def convert_kelvin_to_celsius(deg_f):
    return "{:.2f} C".format(deg_f - 273.15)

try:
    city = input("Въведете град в България: \n")

    url = "http://api.openweathermap.org/data/2.5/weather/?q=" + city + ",bg&appid=965acdac1ae64cf06761bb563ad34d96"

    print('...получаваме информация за времето...')
    print()

    r = requests.get(url, timeout=10)
    content = r.json()
    if r.status_code != 200 \
            or (content['sys']['country'] != 'BG' and content['sys']['country'] != 'Bulgaria') \
            or content['name'] != city:
        raise Exception("Може да сте въвели невалидни данни. Опитайте пак!")

    unix = content['dt']
    date = datetime.fromtimestamp(unix, tz=timezone.utc)
    date = date.strftime("%d.%m.%Y %H:%M")

    main_info = content['main']
    wind = content['wind']

    print("Информация към", date)
    print("Температура:", convert_kelvin_to_celsius(main_info['temp']))
    print("Налягане:", main_info['pressure'])
    print("Влажност:", "{}%".format(main_info['humidity']))
    print("Вятър:", "{} м/с".format(wind['speed']))

    r.close()

except Exception as e:
    print("Грешка:", e)


