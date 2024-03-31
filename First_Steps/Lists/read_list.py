# this program reads a file's contenst 

def main():

    # open a file for reading

    infile = open(r'C:\Users\javie\Downloads\College\Programing projects\Lists\cities.txt', 'r')

    # read the contents of the file into a list
    cities = infile.readlines()

    # close the file
    infile.close()

    # strip the \n from each element. Output is goign to be all cities in line acrsso

    index = 0

    # len is the lenght of the list

    while index < len(cities):

        cities[index] = cities[index].rstrip('\n')

        index += 1

    print(cities)

main()