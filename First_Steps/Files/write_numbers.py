# this program demonstrates how numbers
#must be converted to strings before
# they are written to the text file

def main():
    outfile = open(r'C:\Users\javie\Downloads\College\Programing projects\Files\Numbers.txt', 'w')

    #Get 3 numbers from the user

    num1 = int(input('Enter a number: '))

    num2 = int(input('Enter another number: '))

    num3 = int(input('Enter the Last number: '))

    #Write the numbers to a file

    outfile.write(str(num1) + '\n')     #we are writing numbers to a file 
                                        #so we must use the str function to
                                        #  convert the numbers to a string
    outfile.write(str(num2) + '\n')

    outfile.write(str(num3) + '\n')

    #Close file

    outfile.close()
    print('Data written')

main()
