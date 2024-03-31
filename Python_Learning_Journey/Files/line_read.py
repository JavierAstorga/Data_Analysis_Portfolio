def main():
    #Open the files Names.txt

    infile = open(r'C:\Users\javie\Downloads\College\Programing projects\Files\NewNames.txt', 'r')

    #Read 3 lines from the file

    line1 = infile.readline()        #The readline()puts a \n on to the name

    line2 = infile.readline()   

    line3 = infile.readline()   

    #close file

    infile.close()

    #print the information

    print(line1)
    print(line2)
    print(line3)

main()