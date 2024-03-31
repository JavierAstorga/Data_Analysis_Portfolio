# this program displays 5 random numbers in the range  of 1 through

import random

def main():
    for count in range(500000):

        #Get the random number

        number = random.randint(1,10)

        #displays the number

        print('The number is ', number)

main()