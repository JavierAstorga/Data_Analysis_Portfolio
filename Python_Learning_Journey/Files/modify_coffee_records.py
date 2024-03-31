# this program allows the user to modify
#the quantity in a record in the coffee.txt file

import os # Needed for the removal and rename functions

def main():

    # Create bool Variable as Flag

    found = False

    # get the Search Value and the New Quantity

    search = input('Enter the Description to Search for: ')

    new_qty = int(input('Enter the New Quantity : '))

    # Open the coffee.txt file

    coffee_file = open(r'C:\Users\javie\Downloads\College\Programing projects\Files\coffee.txt', 'r')

    # open up a temp.txt file

    temp_file = open(r'C:\Users\javie\Downloads\College\Programing projects\Files\temp.txt', 'w')

    # read the First Record's Description Field

    descr = coffee_file.readline()

    # Read the rest of the File

    while descr != '':  #while we are not at the end of the file

        #Read the quantity

        qty = float(coffee_file.readline())

        #strip the \n from the description

        descr = descr.rstrip('\n')

        #Write either this record to the Temporary file or the new record if
        #  this is the one that is to be modified

        if descr == search:

            #Write the Modified Record to the Temp File

            temp_file.write(descr + '\n')

            temp_file.write(str(new_qty) + '\n')

            # set the flag to True

            found = True

        else:

            # write the Original Record to the Temp File

            temp_file.write(descr + '\n')

            temp_file.write(str(qty) + '\n')

        # Read the Next Record

        descr = coffee_file.readline()

    #Close both file

    coffee_file.close()

    temp_file.close()

    # Delete the Original coffee.txt file

    os.remove(r'C:\Users\javie\Downloads\College\Programing projects\Files\coffee.txt')

    #Rename Temp file to coffee.txt

    os.rename(r'C:\Users\javie\Downloads\College\Programing projects\Files\temp.txt', r'C:\Users\javie\Downloads\College\Programing projects\Files\coffee.txt')

    # if the search value was not found display a message

    if found: 
        print('The file was UPDATED')

    else:

        print('That item was Not Found in the File')

main()