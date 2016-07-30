# Задача: 3. Анализ на данни от верига магазини - using sysargv

import sys
import csv
import iso8601
from datetime import datetime, timezone

count = 0
total = 0
dates = []
category_dict = {}
category_sales = {}
sales_by_category = []
city_sales = {}
sales_by_city = []
hour_sales = {}
sales_by_hour = []


def add_to_dict(sales_dict, keys, values):
    if keys not in sales_dict:
        sales_dict[keys] = values
    else:
        sales_dict[keys] += values
    return sales_dict


def append_top_items(sales_dict: dict, sales_array: list):
    for keys, values in sales_dict.items():
        sales_array.append(values)
    sales_array.sort()
    top_array = sales_array[:-6:-1]
    return top_array


def print_values(sales_array: list, sales_dict: dict):
    for item in sales_array:
        for keys, values in sales_dict.items():
            if values == item:
                print('\t {} {:.2f}'.format(keys, item))

try:
    if len(sys.argv) < 3:
        raise Exception(
            'You need to provide files as system arguments in the terminal:'
            ' python analyze.py <catalog_file> <sales_file>')
    else:
        catalog_file = sys.argv[1]
        sales_file = sys.argv[2]

        with open(catalog_file, encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 8:
                    product_id = row[0]
                    product_category = row[5]
                    if product_category not in category_dict:
                        category_dict[product_category] = [product_id]
                    else:
                        category_dict[product_category].append(product_id)

        with open(sales_file, encoding='utf-8') as p:
            reader = csv.reader(p)
            for row in reader:
                    if len(row) == 5:
                        product_id2 = row[0]
                        city = row[2]
                        date = iso8601.parse_date(row[3]).replace(minute=0, second=0, microsecond=0)
                        date_norm = date.astimezone(timezone.utc)  # - can be used in place of 'date'
                        dates.append(date)
                        sales_sum = float(row[-1])
                        count += 1
                        total += sales_sum
                        average = total / count
                        for key, value in category_dict.items():
                            if product_id2 in value:
                                add_to_dict(category_sales, key, sales_sum)
                        add_to_dict(city_sales, city, sales_sum)
                        add_to_dict(hour_sales, date, sales_sum)

            dates.sort()
            start_date = dates[0]
            end_date = dates[-1]

            top5_categories = append_top_items(category_sales, sales_by_category)

            top5_cities = append_top_items(city_sales, sales_by_city)

            top5_hours = append_top_items(hour_sales, sales_by_hour)

        print()
        print('Обобщение')
        print('-' * len('Обобщение'))
        print('\tОбщ брой продажби: {}'.format(count))
        print('\tОбщо сума продажби: {:.2f}'.format(total))
        print('\tСредна цена на продажба: {:.2f}'.format(average))
        print('\tНачало на период на данните: {}'.format(start_date.isoformat()))
        print('\tКрай на период на данните: {}'.format(end_date.isoformat()))
        print()
        print('Сума на продажби по категории (top 5)')
        print('-' * 29)
        print_values(top5_categories, category_sales)
        print()
        print('Сума на продажби по градове (top 5)')
        print('-' * 29)
        print_values(top5_cities, city_sales)
        print()
        print('Сума на продажби по час (top 5)')
        print('-' * 29)
        print_values(top5_hours, hour_sales)

except Exception as e:
    print('Invalid data:', e)


