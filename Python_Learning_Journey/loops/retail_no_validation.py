# this program calculates retail prices
#there is no validation done

mark_up = 2.5       #The markup percentage

another = 'y'       #variable to control the loop

#process one or more items

while another == 'y' or another == 'Y':

    #get the items wholesale cost

    wholesale = float(input("Enter the Item's wholesale cost: "))

    #calculate the retail price

    retail = wholesale * mark_up

    #display the retail

    print(f'Retail prices: ${retail:.2f}')

    #do this again

    another = input('Do you want another item? Enter y or Y: ')