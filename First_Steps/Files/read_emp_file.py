#This programs displays the records that are in the employee.txt file

def main():
    # open the file employee.txt

    emp_file = open(r'C:\Users\javie\Downloads\College\Programing projects\Files\employee.txt', 'r')

    # read the first line from the file which is the name

    name = emp_file.readline()

    while name != '':       # not at end of file [EOF]

        #read the id number

        id_num = emp_file.readline()

        #Read the Dept

        dept = emp_file.readline()

        #strip the newlines from the Fields

        name = name.rstrip('\n')

        id_num = id_num.rstrip('\n')

        dept = dept.rstrip('\n')

        #Display the records

        print('Name : ' , name)

        print('ID: ', id_num)

        print('Dept: ', dept)

        # Read the name field for the next record

        name = emp_file.readline()

    #Close file
    emp_file.close

main()