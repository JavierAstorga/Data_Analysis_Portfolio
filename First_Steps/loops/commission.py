# This program 



keep_going = 'y'

# Calculate a series of commissions

while keep_going == 'y':         # Colon allows for indendition

    #Get the Salesman's sales and Commssion rate

    sales = float(input('Enter the amount of Sales: '))

    comm_rate = float(input('Enter the Commission Rate: '))

    # Calculate the commission

    commission = sales * comm_rate

    #Display the Commission

    print(f'The commission is $ {commission:.2f}', sep='')

    # See if the user wants to do another app

    keep_going = input('Do you want to calculate another commission (y for yes)')

