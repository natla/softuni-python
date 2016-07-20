import requests

try:
    #currency = 'GBP'
    #money = 15.34
    currency = input("Въведете валута: \n")
    try:
        amount = float(input("Въведете сума: \n"))
    except:
        raise Exception("Не сте въвели сумата правилно!")

    print('...получаваме информация за валутни курсове...')  # info for the users while they are waiting
    print()
    exchange_rates = requests.get('http://api.fixer.io/latest?base=BGN', timeout=10)
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
            raise Exception('Няма такава валута или въвеждате BGN!')

    result = amount / foreign_rate

    print("Равностойност в BGN: ", result)

    exchange_rates.close()

except Exception as e:
    print('Имате грешка:', e)



