import requests
from datetime import datetime
import pytz

try:
    city = input("Въведете град в България: \n")

    url = "http://api.openweathermap.org/data/2.5/weather/?q=" + city + ",bg&units=metric&appid=c1d344dc9eb1db61f225488045d115be"

    print('...получаваме информация за времето...')
    print()

    r = requests.get(url, timeout=10)
    content = r.json()
    if r.status_code != 200 \
            or (content['sys']['country'] != 'BG' and content['sys']['country'] != 'Bulgaria') \
            or content['name'] != city:
        raise Exception("Може да сте въвели невалидни данни. Опитайте пак!")

    unix = content['dt']
    zone_sofia = pytz.timezone("Europe/Sofia")
    date = datetime.fromtimestamp(unix, tz=zone_sofia)  # we set the timezone to UTC+02:00
    date = date.strftime("%d.%m.%Y %H:%M")

    main_info = content['main']
    wind = content['wind']

    print("Информация към", date)
    print("Температура:", "{}°C".format(main_info['temp']))
    print("Налягане:", main_info['pressure'])
    print("Влажност:", "{}%".format(main_info['humidity']))
    print("Вятър:", "{} м/с".format(wind['speed']))

    r.close()

except Exception as e:
    print("Грешка:", e)


