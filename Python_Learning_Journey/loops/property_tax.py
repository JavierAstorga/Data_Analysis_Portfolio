# this program displays property taxes

tax_factor = 0.0065     #representt the tax factor

# get the first lot number

print('Enter the property lot number\nOr enter 0 to  End: ')

lot = int(input('Enter Lot Number:'))

# Continues processign as long as the user does not enter lot number 0

while lot !=0:       #While lot is not equal to zero fo the following staterments 
                    #If lot was equal to zero then terminate program

    # get the property value...

    value =float(input('Enter the property Value: '))
    
    #Calculate the property's tax

    tax = value * tax_factor

    # display the tax

    print(f'Property tax: $ {tax:.2f}', sep="")

    # get the nex lot number

    print('Enter the next lot number or \nEnter 0 to end:')

    lot = int(input('Lot Number: '))

