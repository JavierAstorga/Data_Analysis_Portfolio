# this program calculate the gross pay for each of the baristas

# num_employees is used as a constant for the size of the list

num_employees = 6

def main():

    # create a list to hold employee hours

    hours = [0] * num_employees

    # get each employee's hours worked

    # populating the hours list

    for index in range(num_employees):

        print('Enter the hours worked by Employee', index + 1, ':', sep='')

        hours[index] = float(input())

    #get the hourly pay rate

    pay_rate = float(input('Enter the hourly pay Rate'))

    # display each employee's gross pay

    for index in range(num_employees):

        gross_pay = hours[index] * pay_rate

        print('Gross pay fpr employee', index + 1, ': $', format(gross_pay, '.2f'))

main()