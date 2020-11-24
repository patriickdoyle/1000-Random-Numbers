#random_list.py
#Assignment for CSCI 111-900
#Last edited 10/7/19 by Pat Doyle

import random

#Program uses random numbers

my_list = []

#Creates empty list

while (len(my_list) < 1000):

    my_list.append(random.randrange(0,101))

    #Loops while the length of this list is less than 1000
    #Appends values between 0 and 101 to list

for element in my_list:
    
    total = sum(my_list)
    minimum = min(my_list)
    maximum = max(my_list)
    average = sum(my_list)/len(my_list)

#for statement iterates the list and calculates values for variables
    
print ("Sum: ", total)
print("Minimum: ", minimum)
print("Maximum: ", maximum)
print("Average: ", average)
    
#Prints values     

