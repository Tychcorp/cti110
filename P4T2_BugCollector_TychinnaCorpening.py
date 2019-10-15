# Create a loop displaying the number of bugs collected during five days
# 10/14/2019
# CTI-110 P4T2 - Bug Collector
# Tychinna Corpening
#

   
# Input bugs collected for a day
# Add bugs collected to total
# Display total

# Initialize the accumulator.
total = 0

# Get the bugs collected for each day.
for day in range(1, 6):
    # Prompt the user.
    print("Enter the bugs collected on day", day)

    # Input the number of bugs.
    bugs = int(input())

    # Add bugs to total.
    total = total + bugs

# Display the total bugs.
print('You collected a total of', total, 'bugs.')
