#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# FIXME: Write the split_check function. HINT: Calculate the amount of tip and tax,
# add to the bill total, then divide by the number of diners.

# Write a split_check function that returns the amount that 
# each diner must pay to cover the cost of the meal.

# The function has four parameters:

# bill: The amount of the bill.
# people: The number of diners to split the bill between.
# tax_percentage: The extra tax percentage to add to the bill.
# tip_percentage: The extra tip percentage to add to the bill.
# The tax or tip percentages are optional and may not be given when calling split_check. 
# Use default parameter values of 0.15 (15%) for tip_percentage, and 0.09 (9%) for tax_percentage. 
# Assume that the tip is calculated from the amount of the bill before tax.

def split_check(bill, people, tax_percentage = 0.09, tip_percentage = 0.15):
    
    tip = tip_percentage * bill
    
    check = ((tax_percentage * bill) + bill + (tip_percentage * bill)) / people
    
    return check

bill = float(input())
people = int(input())

# Cost per diner at the default tax and tip percentages
print(f'Cost per diner: ${split_check(bill, people):.2f}')

bill = float(input())
people = int(input())
new_tax_percentage = float(input())
new_tip_percentage = float(input())

# Cost per diner at different tax and tip percentages
print(f'Cost per diner: ${split_check(bill, people, new_tax_percentage, new_tip_percentage):.2f}')


# In[ ]:




