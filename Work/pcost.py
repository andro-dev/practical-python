# pcost.py
#
# Exercise 1.27 - 1.33

import sys

def portfolio_cost(filename):
    total_cost = 0
    line_counter = 0
    with open(filename, 'rt') as f:
        #cost of a stock = shares * price
        next(f) # skip the header row
        for line in f:
            line_counter += 1
            print(line_counter, line)
            row = line.split(',')
            try:
                total_cost += int(row[1]) * float(row[2])
            except ValueError as ve:
                 print("The following Error occrued in line", line_counter, "of the file:", ve)
            # finally:
            #     print("in 'finally' block")
            continue
    return total_cost

if len(sys.argv) == 2:
    file_name = sys.argv[1]
else:
    file_name = 'Data/portfolio.csv'

print("Total cost:", portfolio_cost(file_name))