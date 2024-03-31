# this program demonstrates the 'IN' Operator used with a List

def main():

    # create a list of Products Numbers

    prod_nums = ['V475', 'F987','Q123','R688']

    # get the podcut number to search for

    search = input('Enter a Product Number')

    # determine whether the product number is in the list

    if search in prod_nums:

        print(search, ' Was Found in the List')

    else:
        print(search, 'Wast not FOUND in the List')

main()