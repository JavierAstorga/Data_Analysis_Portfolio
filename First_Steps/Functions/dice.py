# this program simulate the rolling of dice

import random

#constants for the minimun and maximun random numbers

MIN = 1

MAX = 6

def main():

    #Create a variable to control the loop

    again = 'y'

    # Simulate rolling of the dice

    while again == 'y' or again == 'Y':

        print('Rolling the dice....')
        print('....')
        print('....')
        print('....')
        print('The values are : ')

        print(random.randint(MIN,MAX))
        print(random.randint(MIN,MAX))

        #Do another roll of the dice?

        again = input('Roll the dice again? (y = yes): ')

#call the main function

main()
