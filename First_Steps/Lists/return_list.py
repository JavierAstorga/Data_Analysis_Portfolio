 # this progrma uses a function to create a list. the function retrurns a reference to the list

def main():

    # get a list with values stored in it.

    numbers = get_values()

    # display the values in the list 

    print(' The numbers in the list are: ')

    print(numbers)

# the get_values method gets a series of numbers from the user and stores them in a list
# thefunction returns a reference to thelist

def get_values():

    # create an epty list

    values = []

    # create a variable to control the loop

    again = 'Y'

    # get the values from the user and ADD them to the list

    while again.upper() == 'Y':

        # get a number and add it to the list

        num = int(input('Entetr a number: '))

        values.append(num)

        # do yo want to go again?

        print(' Do you want to add another number: ?')

        again = input('y = yes, anything else = no')


    # return with the list

    return values

main()