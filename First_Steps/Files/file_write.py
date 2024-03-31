def main():
    #open fil name "Newnames.txt"

    #This will create a file called new names.txt in the folder Files for WRITE on 
    # r --> raw data, 'w' --> write to file

    outfile = open(r'C:\Users\javie\Downloads\College\Programing projects\Files\NewNames.txt', 'w')


    #Write the names to the file

    outfile.write('Tom\n')      # Write Tom to file NewNames.txt and then go to

    outfile.write('Jane\n')      # Write Tom to file NewNames.txt and then go to

    outfile.write('Joe\n')      # Write Tom to file NewNames.txt and then go to


    #Close the file

    outfile.close

main()