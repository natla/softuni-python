import csv


def raise_prices(price, percent):
    return price + price * percent / 100


try:
    with open("catalogs/catalog_raised_prices.csv", "w", newline="") as p:
        with open("catalogs/catalog_sample.csv") as f:  # the same can be done with catalogs/catalog_full.csv
            rows = csv.reader(f)
            for row in rows:
                if len(row) == 7:  # eliminate empty rows or rows missing information, if any
                    item_num = row[0]
                    item_name = row[1]
                    item_color = row[2]
                    item_activity = row[3]
                    item_type = row[4]
                    item_age = row[5]
                    item_price = float(row[-1])
                    if item_type == "SHOES" or item_type == "BAGS":
                        new_price = raise_prices(item_price, 50)
                    elif item_type == "JACKETS" or item_type == "SWEATSHIRTS":
                        new_price = raise_prices(item_price, 55)
                    elif item_type == "POLO SHIRTS" or item_type == "PANTS":
                        new_price = raise_prices(item_price, 60)
                    elif item_type == "T-SHIRTS" or item_type == "JERSEYS":
                        new_price = raise_prices(item_price, 65)
                    elif item_type == "HEADWEAR" or item_type == "SWIMWEAR":
                        new_price = raise_prices(item_price, 70)
                    else:
                        new_price = raise_prices(item_price, 75)
                    new_price = ("{:.2f}".format(new_price))

                    writer = csv.writer(p)
                    writer.writerow([item_num, item_name, item_color, item_activity, item_type, item_age, new_price])

except Exception as e:
    print("Invalid data:", e)
