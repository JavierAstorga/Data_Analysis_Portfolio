# this programs gets employee data from the user and saves it as records
# in the employee,txt file

def main():
    # get the number of employee records to create

    num_emps = int(input('How many Employee Records do you want to create? : '))

    #Open file for writing

    emp_file = open(r'C:\Users\javie\Downloads\College\Programing projects\Files\employee.txt', 'w')

    # get the employee data and write it to file

    for count in range(1,num_emps + 1):
        # get the data for an employee

        print('Enter Data for Employee #: ', count, sep='')

        name = input('Name: ')

        id_num = input('ID Number : ')

        dept = input('Department : ')

        # Write this data to the file.. emp_file

        emp_file.write(name + '\n') 

        emp_file.write(id_num + '\n') 

        emp_file.write(dept + '\n') 

    # close file

    emp_file.close()

    print('Data Written to the File')


main()