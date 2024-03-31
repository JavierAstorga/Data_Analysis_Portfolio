# this program read the names.txt file and displays them

def main():
    #Open the file for reading

    #this time we are Reading the file NewNames.txt

    #r --> raw data, 'r' --> read

    infile = open(r'C:\Users\javie\Downloads\College\Programing projects\Files\NewNames.txt', 'r')

    # read the File's Contents

    file_contents = infile.read()

    #Close file

    infile.close()

    #Print the coments
    print(file_contents)

main()