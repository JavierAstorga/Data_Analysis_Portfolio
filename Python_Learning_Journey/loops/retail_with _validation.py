#This program calculates retail prices 
#IT contains validation


mark_up = 2.5       #The markup percentage

another = 'y'       #variable to control the loop

#process one or more items

while another == 'y' or another == 'Y':

    #get the items wholesale cost

    wholesale = float(input("Enter the Item's wholesale cost: "))

    #validate the wholesale cost

    while wholesale < 0:
        print('ERROR: The Cost cannot be Negative: ')

        wholesale = float(input("Enter the Item's Wholesale Cost"))
        #Calculate the retail price
    
    retail = wholesale * mark_up

    #Display the retail price

    print(f'The retail price is: ${retail:.2f}')

    #Do you want to go around again?

    another = input('Do you want to keep going? Y or N: ')