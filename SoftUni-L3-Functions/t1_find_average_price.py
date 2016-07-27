total = 0
count = 0
with open('catalogs/catalog_sample.csv') as f:
    for line in f:
        product = line.split(',')
        if product \
                and product[0] \
                and len(product) == 7:
            price = float(product[-1].rstrip())
            total += price
            count += 1
    average = total / count
    print('Average price: {:.2f} for {} items'.format(average, count))

# solution using a list of prices, then sum and len of list
prices = []
with open('catalogs/catalog_full.csv') as f:
    for line in f:
        product = line.split(',')
        if product \
                and product[0] \
                and len(product) == 7:
            prices.append(float(product[-1]))
    average = sum(prices) / len(prices)
    print('Average price: {:.2f} for {} items'.format(average, len(prices)))

