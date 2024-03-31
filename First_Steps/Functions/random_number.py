# this program displays a random number
# in the range of 1 through 10

import random # import the random module, so now you can use all

def main():

    #Get a random number 
    # randint is  method of the random module

    number = random.randint(1,10)

    #display the number

    print('The number is ', number)


main()