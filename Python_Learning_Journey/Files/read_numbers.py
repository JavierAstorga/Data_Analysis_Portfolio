#This prograam demonstrates how numbers that are read from a file
# must be converted from string before they are used in math operations

def main():

    #open the file for reading
    # r --> raw data

    # 'r' --> read

    infile = open(r'C:\Users\javie\Downloads\College\Programing projects\Files\Numbers.txt', 'r')

    #read 3 numbers from the file
    #in the write_number program the user gave 3 numbers which were
    #store in num1, num2, num3.
    #Now we are reading these numbers and converting the numbers to integers.

    num1 = int(infile.readline())

    num2 = int(infile.readline())

    num3 = int(infile.readline())

    #close file

    infile.close()

    #add the number

    total = num1 + num2 + num3
    #Display the numberes and their total
    print('The Numbers are: ', num1, num2, num3)

    print('The total is: ', total)

main()