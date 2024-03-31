# This program reads the contests of the file Friends.txt one line at a time

def main():
    # Open the file Friends.txt

    infile = open(r'C:\Users\javie\Downloads\College\Programing projects\Files\Friends.txt', 'r')

    #Read 3 lines from the file

    line1 = infile.readline()

    line2 = infile.readline()

    line3 = infile.readline()

    # Strip the \n from each string

    line1 = line1.rstrip('\n')

    line2 = line2.rstrip('\n')

    line3 = line3.rstrip('\n')

    #Close file

    infile.close()

    print(line1)
    print(line2)
    print(line3)

main()