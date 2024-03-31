# this program saves a list of strings to a file

def main():

    # create a list of strings

    cities = ['Dublin', 'Cork', 'Belfast', 'Galway']

    # open the file for writing

    # no space between the r and single quote. r--> war data    'w' --> Write


    outfile = open(r'C:\Users\javie\Downloads\College\Programing projects\Lists\cities.txt', 'w')

    # write the list to the file


    for item in cities:

        outfile.write(item + '\n')

        # close file
        # 
    outfile.close()

main() 