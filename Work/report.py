# report.py
#
# Exercise 2.4
import csv
from sys import argv
import sys

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        try:
            headers =next(rows)
            for row in rows:
                name,shares, price = row
                holding = {"name" : name, "shares" : int(shares), "price" : float(price) }
                portfolio.append(holding)
        except Error as e:
            print("Error:", e)

    return portfolio

def main():
    from pprint import pprint
    #see if file name was passed as a 2nd argument from command line
    #ex. python3 report.py Data/portfolio2.csv
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = "Data/portfolio.csv"

    portfolio = read_portfolio(filename)
    pprint(portfolio)



if __name__ == "__main__":    
    main()


