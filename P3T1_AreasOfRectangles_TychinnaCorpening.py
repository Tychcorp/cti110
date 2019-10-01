 # Writing a program that asks the greater length and width of two rectangles.
    # September 23, 2019
    # CTI-110 P3T1 - Areas of Rectangles
    # Tychinna Corpening

# input section
    #input "enter rectangle 1 length and width
    #input "enter rectangle 2 length and width
 
# processing section
    #total = length1 * width1 is area 1
    #total = length2 * width2 is area 2

# output section
    #display "total is" greater area rectangle amount



# Get the dimensions of rectangle 1.
length1 = int(input('Enter the length of rectangle 1: '))
width1 = int(input('Enter the width of rectangle 1: '))


# Get the dimensions of rectangle 2.
length2 = int(input('Enter the length of rectangle 2: '))
width2 = int(input('Enter the width of rectangle 2: '))


# Calculate the area of the rectangles
area1 = length1 * width1
area2 = length2 * width2


# Determine which has the greater area.
if area1 > area2:
    print('Rectangle 1 has the greater area.')
else:
    if area2 > area1:
        print ('Rectangle 2 has the greater area.')
    else:
        print ('Both have the same area.')

