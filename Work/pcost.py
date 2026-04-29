# pcost.py
#
# Exercise 1.27
total_cost = 0
with open('Data/portfolio.csv', 'rt') as f:
    #cost of a stock = shares * price
    next(f) # skip the header row
    for line in f:
        row = line.split(',')
        total_cost += int(row[1]) * float(row[2])

print("Total cost", total_cost)