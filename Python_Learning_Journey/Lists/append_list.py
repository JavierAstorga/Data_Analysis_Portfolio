# this program demonstrates how the append method can be used to add items to a list

def main():

    # first create an empty list

    name_list = []

    # create a variable to control the loop

    again = 'Y'

    # add some names to the list

    while again.upper() == 'Y':

        # get the Name from the user

        name = input('Enter a Name: ')

        # append the name to the list Populating the list.

        name_list.append(name)

        # add another name to the List?

        print('Do you wish to add another name? ')

        again = input('y = yes, anything else = no: \n')

        print()

    #

    print('Here are the Names you entered')

    for name in name_list:

        print(name)

main()