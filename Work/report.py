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
                symbol = row[0]
                nshares = int(row[1])
                price = float(row[2])
                holding = (symbol, nshares, price)
                portfolio.append(holding)
        except Error as e:
            print("Error:", e)

    return portfolio

def main():
    from pprint import pp

    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = "Data/portfolio.csv"
        
    portfolio = read_portfolio(filename)
    pp(portfolio)



if __name__ == "__main__":    
    main()


