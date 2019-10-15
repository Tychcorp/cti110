# Calculate the total meal price to include the tp and tax.
# October 7, 2019
# CTI-110 P3HW2 - Meal Tip Tax Calculator
# Tychinna Corpening

# input section 
  # meal_price = Please enter the charge of food
  # tip amount = 20%
  # tax amount = 6%
  
# processing section 
  # total_price = meal_price + tip + tax
  
# output process
  # display the total sale_price

meal_price = float(input('Please enter the charge of the food:'))
tip = float(input("Enter the tip percentage (.16, .18, .20): "))
tax = meal_price * 0.06

if tip == .16:
    tipAmount = meal_price * tip

elif tip == .18:
    tipAmount = meal_price * tip

elif tip == .20:
    tipAmount = meal_price * tip
else:
    print('You should have entered a tip amount of .16, .18, or .20')
     
total = meal_price + tax + tipAmount

print('The meal price is',format(meal_price,'.2f'))
print('The tip is',format(tipAmount,'.2f'))
print('The tax is',format(tax,'.2f'))
print('The total is',format(total,'.2f'))
