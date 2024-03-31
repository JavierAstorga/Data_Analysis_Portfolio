#this program calculates the lenght of a right 
#triangle's hypotenuse

import math

def main():
        
    #get the legth of the traingle's two sides

    a = float(input('Enter the lenght of side A : '))

    b = float(input('Enter the length of side B : '))

    #calculate the lenght of the Hypotenuse

    #the match module and hypot is used here. The funtcion
    # in this module is hypot

    #math is module ad hypot is function --> math.hypot

    c = math.hypot(a,b)

    #display the lenght of the hypotenuse

    print('The lenght of the Hypotenuse is ', c)
    

main()