#THis program calculates the sum of a series of number
#entered by user

max = 5 #this is maximun number

#initialize an accumulator variables

total = 0

#explain what we are doing

print('This program calculates the sum of\n', max, 'Numbers you will enter')

#Get the numbers and accumulate them

# Range 0 - 4

for counter in range(max):
    number = int(input('Enter a number: '))

    total = total + number

    #Display the total of the numbers

print('The total is: ', total)