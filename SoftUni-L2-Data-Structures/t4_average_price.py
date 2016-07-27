prices = []

while True:
    price = input("Enter a price for the medicine. If you've finished, enter 'stop'\n")
    if price == 'stop':
        break
    # to do - check if price is a valid float
    prices.append(float(price))

if len(prices) < 4:
    print("Not enough data")
else:
    prices.sort()
    lowest = prices.pop(0)
    highest = prices.pop(-1)
    if lowest != highest:
        print('The lowest price is', lowest)
        print('The highest price is', highest)
        for index, price in enumerate(prices):
            if price == highest or price == lowest:
                prices[index] = 0
        if sum(prices) > 0:
            average = sum(prices) / len(prices)
            print('The average price is', average)
        else:
            print('Not enough data to calculate average')
    else:
        print('All prices are equal: ', lowest)

