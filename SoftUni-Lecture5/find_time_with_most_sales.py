from datetime import datetime
import csv

# find the DAY with the most sales:

all_sales = []
daily_sales = {}

with open("sales.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        if row and row[0] and len(row) == 2:
            date = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S.%f")
            weekday = date.strftime("%A")

            if weekday in daily_sales:
                daily_sales[weekday] += float(row[1])
            else:
                daily_sales[weekday] = float(row[1])

for key, value in daily_sales.items():
    all_sales.append(value)
max_sale = max(all_sales)
for key, value in daily_sales.items():
    if value == max_sale:
        print('The day with the most sales is {}: {}' .format(key, max_sale))

# find the HOUR with the most sales:

hourly_sales = {}
all_sales2 = []

with open("sales.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        if row and row[0] and len(row) == 2:
            date = datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S.%f")
            hour = date.time()
            hour = hour.replace(minute=0, second=0, microsecond=0)

            if hour in hourly_sales:
                hourly_sales[hour] += float(row[1])
            else:
                hourly_sales[hour] = float(row[1])

for key, value in hourly_sales.items():
    all_sales2.append(value)
max_sale2 = max(all_sales2)
for key, value in hourly_sales.items():
    if value == max_sale2:
        print('The hour with the most sales is between {} and {}' .format(key.hour, key.hour + 1))
