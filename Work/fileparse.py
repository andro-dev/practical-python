# fileparse.py
#
# Exercise 3.3

import csv

file = '/home/andrew/projects/python/practical-python/Work/Data/missing.csv'


def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=','):
    '''
        Modify the `parse_csv()` function to catch all `ValueError` exceptions
    generated during record creation and print a warning message for rows
    that can’t be converted.

    The message should include the row number and information about the
    reason why it failed.  To test your function, try reading the file
    `Data/missing.csv` above.  For example:

    python
    >>> portfolio = parse_csv('Data/missing.csv', types=[str, int, float])
    Row 4: Couldn't convert ['MSFT', '', '51.23']
    Row 4: Reason invalid literal for int() with base 10: ''
    Row 7: Couldn't convert ['IBM', '', '70.44']
    Row 7: Reason invalid literal for int() with base 10: 
    '''

    if select and has_headers:
        raise RuntimeError("select argument requires column headers")
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f, delimiter=delimiter)
        print(f)

        # Read the file headers (if any)
        headers = next(rows) if has_headers else []

        # If specific columns have been selected, make indices for filtering 
        if select:
            indices = [ headers.index(colname) for colname in select ]
            headers = select

        records = []
        for row_num, row in enumerate(rows, start=1):
            if not row:     # Skip rows with no data
                continue

            # If specific column indices are selected, pick them out
            if select:
                try:
                    row = [ row[index] for index in indices]
                except IndexError:
                    print(f"Row {rows.line_num}: Column index out of range")
                    continue

            # Apply type conversion to the row
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    print(f"Row {rows.line_num}: Couldn't convert {row}")
                    print(f"Row {rows.line_num}: Reason {e}")
                    continue

            # Make a dictionary or a tuple
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

        return records



    pass

try:
    parse_csv(file, types=[str, int, float])
except RuntimeError as e:
    print("\nRuntimeError:", e)
finally:
    print("\nThis is the finally block, it always runs.")


# parse_csv('stocks.csv', select=['symbol', 'price'], types=[str, float])
