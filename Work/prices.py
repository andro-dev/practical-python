#exercise 2.6

#prices.py

import csv
import sys


def read_prices(filename="Data/prices.csv"):
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        prices = {}
        for row in rows:
            try:
                if row:
                    name, price = row[0], row[1]
                    print(f"{name} {price}")
                    prices[name] = float(price)
            except Exception as e:
                print("Exception:", e)
            continue
    return prices
        
if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = "/home/andrew/projects/python/practical-python/Work/Data/prices.csv"
    read_prices(filename)