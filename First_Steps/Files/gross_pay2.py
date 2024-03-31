

def main():

    try:

        #Get the numbers of hours worked

        hours = int(input('Enter the number of hours worked'))

        # get the hourly pay rate

        pay_rate = float(input('Enter the hourly pay rate '))

        # Calculate the Gross Pay

        gross_pay = hours * pay_rate

        # Display Gross Pya

        print(f'Gross Pay is: $ {gross_pay:.2f}' )

    except ValueError:

        print(' ERROR: Hours Worked and Hourly Rate must be Valid Integers')

main()