# This programs reads all of the values in the sales.txt file

def main():
    #open file for reading

    sales_file = open(r'C:\Users\javie\Downloads\College\Programing projects\Files\Sales.txt', 'r')

    #Read the first line from the file but it doesn't convert to a number yet. We still need to test
    # for an empty string EOF

    line = sales_file.readline()

    #As long as an empty string EOF is not returned from readline, continue processing

    while line != '':   #While not at the end of the file EOF

        #convert line to a FloatingPoint

        amount = float(line)

        #format and display the amount

        print(format(amount, '.2f'))

        #read the next line

        line = sales_file.readline()

    #close the file

    sales_file.close()

main()