# Find average price of products in a text file, grouped by sex and age
# Infant, Kid, Men, Unisex, Woman


def average(prices):
    return sum(prices) / len(prices)

infant_prices = []
kid_prices = []
men_prices = []
unisex_prices = []
woman_prices = []

with open('catalogs/catalog_sample.csv') as f:
    for line in f:
        product = line.split(',')
        if product \
                and product[0] \
                and len(product) == 7:
            if "Infant" in product:
                infant_prices.append(float(product[-1]))
            elif "Kid" in product:
                kid_prices.append(float(product[-1]))
            elif "Men" in product:
                men_prices.append(float(product[-1]))
            elif "Unisex" in product:
                unisex_prices.append(float(product[-1]))
            elif "Woman" in product:
                woman_prices.append(float(product[-1]))

    print('Infant average price: {:.2f} for {} items'.format(average(infant_prices), len(infant_prices)))
    print('Kid average price: {:.2f} for {} items'.format(average(kid_prices), len(kid_prices)))
    print('Men average price: {:.2f} for {} items'.format(average(men_prices), len(men_prices)))
    print('Unisex average price: {:.2f} for {} items'.format(average(unisex_prices), len(unisex_prices)))
    print('Woman average price: {:.2f} for {} items'.format(average(woman_prices), len(woman_prices)))

print()
# bigger catalog:

infant_prices = []
kid_prices = []
men_prices = []
unisex_prices = []
woman_prices = []

with open('catalogs/catalog_full.csv') as f:
    for line in f:
        product = line.split(',')
        if product \
                and product[0] \
                and len(product) == 7:
            if "Infant" in product:
                infant_prices.append(float(product[-1]))
            elif "Kid" in product:
                kid_prices.append(float(product[-1]))
            elif "Men" in product:
                men_prices.append(float(product[-1]))
            elif "Unisex" in product:
                unisex_prices.append(float(product[-1]))
            elif "Woman" in product:
                woman_prices.append(float(product[-1]))

    print('Infant average price: {:.2f} for {} items'.format(average(infant_prices), len(infant_prices)))
    print('Kid average price: {:.2f} for {} items'.format(average(kid_prices), len(kid_prices)))
    print('Men average price: {:.2f} for {} items'.format(average(men_prices), len(men_prices)))
    print('Unisex average price: {:.2f} for {} items'.format(average(unisex_prices), len(unisex_prices)))
    print('Woman average price: {:.2f} for {} items'.format(average(woman_prices), len(woman_prices)))
