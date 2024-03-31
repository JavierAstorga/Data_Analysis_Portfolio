# This program displays the records in the coffee.txt file

def main():

    #open the coffee.txt file

    coffee_file = open(r'C:\Users\javie\Downloads\College\Programing projects\Files\coffee.txt', 'r')

    # read the first record's descripion field

    descr = coffee_file.readline()
    
    #Read the rest of the file

    while descr != '':

        # Read the qty field

        qty = float(coffee_file.readline())

        #strip the \n from the description

        descr = descr.rstrip('\n')

        #display the record

        print('Description : ', descr)

        print('Quantity : ', qty)

        #read the next rcord

        descr = coffee_file.readline()

    coffee_file.close()

    print('Data Read    ')

main()