# This program reads numbers from a file into a list

def main():

    # open file for reading

    infile = open(r'C:\Users\javie\Downloads\College\Programing projects\Lists\numbers.txt', 'r')

    numbers = infile.readlines()

    # close file

    infile.close()

    # convert each element to an integer

    index = 0 

    while index < len(numbers):

        numbers[index] = int(numbers[index])

        index = index + 1

    # print list

    print(numbers)

main()