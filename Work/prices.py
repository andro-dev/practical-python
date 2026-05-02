#exercise 2.6

#prices.py

import csv
import sys


def read_prices(filename="Data/prices.csv"):
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        for i, row in enumerate(rows, 1):
            try:
                if row:
                    print(f"{i} {row}")
            except Exception as e:
                print("Exception:", e)
            continue
        
if __name__ == "__main__":
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = "/home/andrew/projects/python/practical-python/Work/Data/prices.csv"
    read_prices(filename)