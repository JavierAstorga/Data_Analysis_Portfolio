# this pogram ADDS coffee inventory Records to the coffee.txt file

def main():
    # Crate a variable to control the loop

    another = 'y'

    #Open the coffee.txt file in APPEND mode

    coffee_file = open(r'C:\Users\javie\Downloads\College\Programing projects\Files\coffee.txt', 'a')

    # Add records to the file

    while another == 'y' or another == 'Y':

        # get the coffee record data

        print('Enter the following Coffee Data')

        descr = input('Description')

        qty = int(input('Quantity (in pounds) : '))

        #Append the Data to the File

        coffee_file.write(descr + '\n')

        coffee_file.write(str(qty)+ '\n')

        # determine whether the user wants to add another record to the fil

        print('Do you want to add Another Record? ')

        another = input('Y = yes, anything else = no : ')

    #close the file

    coffee_file.close()

    print('Data Written')

main()