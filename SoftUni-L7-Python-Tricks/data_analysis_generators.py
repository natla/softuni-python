import csv
import iso8601

CATALOG_FILENAME = 'sales-analysis-assignment/catalog.csv'
SALES_FILENAME = 'sales-analysis-assignment/sales-10K.csv'

COLUMN_ITEM_ID = 0
COLUMN_COUNTRY = 1
COLUMN_CITY = 2
COLUMN_TS = 3
COLUMN_PRICE = 4

COLUMN_CATEGORY = 5

KEY_ITEM_ID = 'item_id'
KEY_COUNTRY = 'country'
KEY_CITY = 'city'
KEY_TS = 'ts'
KEY_PRICE = 'price'


def main():
    catalog = load_catalog(CATALOG_FILENAME)

    total_count = 0
    total_amount = 0
    min_timestamp = None
    max_timestamp = None

    load_sales_generator_object = load_sales(SALES_FILENAME)
    for sale in load_sales_generator_object:
        total_amount += sale[KEY_PRICE]
        total_count += 1
        ts = sale[KEY_TS]

        if min_timestamp is None or ts < min_timestamp:
            min_timestamp = ts
        if max_timestamp is None or ts > max_timestamp:
            max_timestamp = ts

    print("""
Обобщение
---------
    Общ брой продажби: {total_count}
    Общо сума продажби: {total_amount:.2f} €
    Средна цена на продажба: {average_price:.2f} €
    Начало на период на данните: {min_ts}
    Край на период на данните: {max_ts}""".format(
        total_count=total_count,
        total_amount=total_amount,
        average_price=total_amount / total_count if total_count else None,
        min_ts=min_timestamp.isoformat(),
        max_ts=max_timestamp.isoformat(),
    ))

    load_sales_generator_object = load_sales(SALES_FILENAME)
    print_top_by_category(load_sales_generator_object, catalog)

    load_sales_generator_object = load_sales(SALES_FILENAME)
    print_top_by_cities(load_sales_generator_object)

    load_sales_generator_object = load_sales(SALES_FILENAME)
    print_top_by_hour(load_sales_generator_object)


def load_catalog(filename: str) -> dict:
    result = {}
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            item_id = row[COLUMN_ITEM_ID]
            category = row[COLUMN_CATEGORY]
            result[item_id] = category
    return result


def load_sales(filename: str) -> dict:
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            sale = {}
            sale[KEY_ITEM_ID] = row[COLUMN_ITEM_ID]
            sale[KEY_COUNTRY] = row[COLUMN_COUNTRY]
            sale[KEY_CITY] = row[COLUMN_CITY]
            sale[KEY_TS] = iso8601.parse_date(row[COLUMN_TS]).replace(minute=0, second=0, microsecond=0)
            sale[KEY_PRICE] = float(row[COLUMN_PRICE])
            yield sale


def print_top_by_category(sales, catalog):
    amounts_by_category = {}  # key : category name  ,  value : accumulated sum of sales

    for sale in sales:
        item_id = sale[KEY_ITEM_ID]
        price = sale[KEY_PRICE]
        category_name = catalog.get(item_id, None)
        if category_name not in amounts_by_category:
            amounts_by_category[category_name] = 0
        amounts_by_category[category_name] += price

    amounts_by_category_sorted = []
    for category_name, total_amount in amounts_by_category.items():
        amounts_by_category_sorted.append((total_amount, category_name))

    amounts_by_category_sorted.sort(reverse=True)

    print("""
Сума на продажби по категории (top 5)
-----------------------------""")
    for total_amount, category_name in amounts_by_category_sorted[:5]:
        print("    {}: {:.2f} €".format(category_name, total_amount))


def print_top_by_cities(sales):
    amounts_by_city = {}  # key : city name  ,  value : accumulated sum of sales

    for sale in sales:
        city_name = sale[KEY_CITY]
        price = sale[KEY_PRICE]
        if city_name not in amounts_by_city:
            amounts_by_city[city_name] = 0
        amounts_by_city[city_name] += price

    amounts_by_city_sorted = []
    for city_name, total_amount in amounts_by_city.items():
        amounts_by_city_sorted.append((total_amount, city_name))

    amounts_by_city_sorted.sort(reverse=True)

    print("""
Сума на продажби по градове (top 5)
-----------------------------""")
    for total_amount, city_name in amounts_by_city_sorted[:5]:
        print("    {}: {:.2f} €".format(city_name, total_amount))


def print_top_by_hour(sales):
    amounts_by_hour = {}  # key : hour  ,  value : accumulated sum of sales

    for sale in sales:
        hour = sale[KEY_TS]
        price = sale[KEY_PRICE]
        if hour not in amounts_by_hour:
            amounts_by_hour[hour] = 0
        amounts_by_hour[hour] += price

    amounts_by_hour_sorted = []
    for hour, total_amount in amounts_by_hour.items():
        amounts_by_hour_sorted.append((total_amount, hour))

    amounts_by_hour_sorted.sort(reverse=True)

    print("""
Сума на продажби по час (top 5)
-----------------------------""")
    for total_amount, hour in amounts_by_hour_sorted[:5]:
        print("    {}: {:.2f} €".format(hour, total_amount))


if __name__ == '__main__':
    main()
