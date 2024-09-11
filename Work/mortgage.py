# mortgage.py
#
# Exercise 1.7

# pay an extra $1000/month for the first 12 months
# print the number of months required to payoff the mortgage


principal = 500000.0
rate = 0.05
payment = 2684.11
extra_payment = 1000
extra_payment_start_month = 61
extra_payment_end_month = 108
months = 0
months_with_extra_payment = 12
total_paid = 0.0

while principal > 0:
    months = months + 1
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment

    if extra_payment_start_month <= months <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    if principal < 0:
        total_paid = total_paid + principal # return overpaid money
        principal = 0

    print(months, round(total_paid,2), round(principal,2))

print('Total paid', round(total_paid, 1))
print('Total months', months)