# this program converts cups to fluid ounces
# all methods/ functions/ procedures are on left hand side

def main(): 
    #display intro screen

    intro()

    #get number of cups

    cups_needed = int(input('Enter the number of cups: '))

    # convert the cups to ounces

    cups_to_ounces(cups_needed)

# the intro function displays and introductory screen

def intro():
    print('This program converts measurements \n'
           'in cups to fluid ounces. For your reference'
           '\n 1 cup = 8 fluid ounces')
    
    print()

# the cups_to_ounces function accepts a number of
#cups amd displays the equivalent number of ounces

def cups_to_ounces(cups):
    ounces = cups * 8

    print(f'That converst to {ounces} ounces')


#Call the main function
main()