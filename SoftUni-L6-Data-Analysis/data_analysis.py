# Задача: 3. Анализ на данни от верига магазини

import csv
import iso8601
from datetime import datetime, timezone

total = 0
dates = []
category_dict = {}
category_sales = {}
city_sales = {}
hour_sales = {}


def add_to_dict(sales_dict, keys, values):
    """
    function for creating dictionaries based on product categories, cities and dates,
    and adding the total of sales for each of them
    """
    if keys not in sales_dict:
        sales_dict[keys] = values
    else:
        sales_dict[keys] += values
    return sales_dict


def append_top_items(sales_dict: dict):
    """
    function for finding the top 5 categories, cities and hours based on the total of sales
    """
    sales_array = [(values, keys) for keys, values in sales_dict.items()]
    sales_array.sort(reverse=True)
    return sales_array[:5]


def print_values(sales_array: list):
    """
    formatted printing of the top 5
    """
    print("\n".join(["\t{} {:.2f} €".format(keys, values) for values, keys in sales_array]))

try:
    with open('sales-analysis/catalog.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) == 8:
                product_id = row[0]
                product_category = row[5]
                if product_category not in category_dict:
                    category_dict[product_category] = [product_id]
                else:
                    category_dict[product_category].append(product_id)

    with open('sales-analysis/sales-10K.csv', encoding='utf-8') as p:
        reader = csv.reader(p)
        for row in reader:
            if len(row) == 5:
                product_id2 = row[0]
                city = row[2]
                date = iso8601.parse_date(row[3]).replace(minute=0, second=0, microsecond=0)
                date_norm = date.astimezone(timezone.utc)  # - can be used in place of 'date'
                dates.append(date)
                sales_sum = float(row[-1])
                total += sales_sum
                for key, value in category_dict.items():
                    if product_id2 in value:
                        add_to_dict(category_sales, key, sales_sum)
                add_to_dict(city_sales, city, sales_sum)
                add_to_dict(hour_sales, date, sales_sum)

        count = len(dates)
        average = total / count

        dates.sort()
        start_date = dates[0]
        end_date = dates[-1]

        top5_categories = append_top_items(category_sales)

        top5_cities = append_top_items(city_sales)

        top5_hours = append_top_items(hour_sales)

    print("""
Обобщение
---------
     Общ брой продажби: {}
     Общо сума продажби: {:.2f} €
     Средна цена на продажба: {:.2f} €
     Начало на период на данните: {}
     Край на период на данните: {}

Сума на продажби по категории (top 5)
-----------------------------"""
          .format(count, total, average, start_date.isoformat(), end_date.isoformat()))
		  
    print_values(top5_categories)

    print("""
Сума на продажби по градове (top 5)
-----------------------------""")
    print_values(top5_cities)

    print("""
Сума на продажби по час (top 5)
-----------------------------""")
    print_values(top5_hours)

except Exception as e:
    print('Invalid data:', e)
