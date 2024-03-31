def main():

    # create list

    numbers = [1,2,3,4,5,6,7]

    # open file for writing

    # r --> raw data,   'w' ---> write

    outfile = open(r'C:\Users\javie\Downloads\College\Programing projects\Lists\numbers.txt', 'w')

    # write the numbers to the file

    for item in numbers:

        # str function. List of numbers are written to a file
        # each item is converted to a string with the str function

        outfile.write(str(item) + '\n' )
    
    # close file

    outfile.close()

main()