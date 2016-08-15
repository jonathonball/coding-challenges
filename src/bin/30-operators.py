#!/usr/bin/python3

import sys

input_data = [x.strip() for x in sys.stdin.readlines()]

meal_cost = float(input_data[0])
tip_percent  = int(input_data[1])
tax_percent  = int(input_data[2])

tip = meal_cost * (tip_percent / 100)
tax = meal_cost * (tax_percent / 100)
total = meal_cost + tip + tax
print("The total meal cost is " + str(round(total)) + " dollars.")

