# this program display the contests of a file 
# Ask the user for the File Name.

def main():

    # get the name of the file from the user

    filename = input('Enter the File Name: ')

    #Open up thefile 

    infile = open(r'C:\Users\javie\Downloads\College\Programing projects\Files\\' + filename, 'r')


    # read the contents

    contents = infile.read()

    #display the contents

    print(contents)

    #close file

    infile.close()

main()