import requests
from datetime import datetime

try:
    date = input("Въведете дата: \n")
    currency = input("Въведете валута: \n")
    try:
        amount = float(input("Въведете сума: \n"))
    except:
        raise Exception("Не сте въвели сумата правилно!")
    base = input("Въведете валута, към която да се конвертира: \n")

    try:
        datetime.strptime(date, "%Y-%m-%d").date()
    except:
        raise Exception('Не сте въвели валидна дата във формат година-месец-ден!')

    url = 'http://api.fixer.io/' + date

    param = {'base': base}

    print('...получаваме информация за валутни курсове...')
    print()
    exchange_rates = requests.get(url, params=param)
    if exchange_rates.status_code != 200:  # i.e. if the HTTP request was not successful
        raise Exception('Невалидна валута, към която да се конвертира!')
    file = exchange_rates.json()

    rates = {}
    for key, value in file.items():
        if key == 'rates':
            rates = value

    foreign_rate = 0
    for key, value in rates.items():
        if key == currency:
            foreign_rate = value
        elif currency not in rates:
            raise Exception('Няма такава валута или въвеждате една и съща валута!')

    result = amount / foreign_rate

    print("Равностойност в {}: {:.2f}".format(base, result))

    exchange_rates.close()

except Exception as e:
    print('Имате грешка:', e)
