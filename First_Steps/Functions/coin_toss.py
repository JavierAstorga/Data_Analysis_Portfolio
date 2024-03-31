#This program simulates 10 toasses of a coin

import random

#constants

heads = 1

tails = 2

tosses = 10

def main():

    for toss in range(tosses):

        ## Simulates the coin toss
        if random.randint(heads,tails) == heads:

            #if a random number in range of
            # 1 - 2 and = 1 
            #Then heads otherwise tails 
             print('Heads')

        else:
        
            print('Tails')

main()

