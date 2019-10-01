# This is to calculate the total amount of a meal purchased
# September 16, 2019
# CTI-110 P2HW1 - Meal Tip Tax Calculator
# Tychinna Corpening


# input section 
  # meal_price = 100
  # tip amount = 15%
  # tax amount = 6%
  
# processing section 
  # sale_price = meal_price + tip + tax
  
# output process
  # display the total sale_price

# Get the item's meal price
meal_price = float(input("Enter the meal price:"))
tip_percentage = float(input("Enter the tip percentage:"))
tax_percentage = float(input("Enter the tax percentage:"))

# Calculate the amount of the tip
tip = meal_price * tip_percentage

# Calculate the amount of the tax
tax = meal_price * tax_percentage

# Calculate the sale price
sale_price = meal_price + tip + tax

# Display the sale price
print('The sale price is',format(sale_price,'.2f'))
print('The tip is',format(tip,'.2f'))
print('The tax is',format(tax,'.2f'))




    
