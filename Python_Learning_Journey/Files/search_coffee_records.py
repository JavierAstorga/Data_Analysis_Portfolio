#This program allows the user to search the coffee.txt file for records matching a description

def main():

    #create a bool variable to usea a flag. True or false

    found = False

    #get the search value

    search = input('Enter a description to search for: ')

    # Open the coffe.txt file

    coffee_file = open(r'C:\Users\javie\Downloads\College\Programing projects\Files\coffee.txt', 'r')

    # read the first record's description field

    descr = coffee_file.readline()

    #read the rest of the file

    while descr != '':

        #read the quantity field

        qty = float(coffee_file.readline())

        #strip \n from the description field

        descr = descr.rstrip('\n')

        #determine whether this record matches the search value

        if descr == search:

            #display the record

            print('Description : ', descr)

            print('Quantity ', qty)

            #set the found flag totrue

            found = True

            # read the next desce record

        descr = coffee_file.readline()

    #close file

    coffee_file.close()

    # if the search value was not found in the file display a message

    if not found:

        print('That Item was Not Found in the File')

main()