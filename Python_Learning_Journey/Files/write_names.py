# This program gets 3 namesfrom the user

# # and writes them to a file

def main():
    # Get the 3 names

    print('Enter 3 of your Friend names')

    name1 = input('Friend 1: ')

    name2 = input('Friend 2: ')

    name3 = input('Friend 3: ')

    # open the file for Writing

    myfile = open(r'C:\Users\javie\Downloads\College\Programing projects\Files\Friends.txt', 'w')

    #write the Names to the file

    #Concatnating the Names with \n   --> \n means new line

    myfile.write(name1 + '\n')      #Write the first name 

    myfile.write(name2 + '\n')      #Write the second name 

    myfile.write(name3 + '\n')      #Write the third name 

    #Close file

    myfile.close()
    print('Data Written to File')

main()