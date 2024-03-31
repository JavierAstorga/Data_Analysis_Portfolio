#This program calculates a slaesperson's pay
#at the company Make my own sound

def main():

    #Get the amount of sales

    sales = get_sales()

    #get the amount of advanced pay

    advanced_pay = get_adv_amount()

    #determine the commission rate

    comm_rate = determine_comm_rate(sales)

    #calculate your pay

    pay = sales * comm_rate - advanced_pay

    #display the amount of pay

    print(f'The pay is {pay:.2f}')


    #determine whether pay is negative

    if pay < 0:
        print('The salesperson must reimburst the company')

#the get_sales function gets a salesperson's monthly sales
#from the user and returns that value

def get_adv_amount():

    print('Enter the amount of advance pay, or\n'
          'Enter 0 if No advance pay was given')
    
    advanced = float(input('Enter Advanced pay: '))

    return advanced

def get_sales():
    input_get_sales = float(input('Enter amount of sales: '))

    return input_get_sales

#the determine-comm-rate function accepts the amount of sales 
#as an argument and returns the aplication comm rate

def determine_comm_rate(sales):

    #determine the commision rate

    if sales < 10000.0:

        rate = .10

    elif sales >= 10000 and sales <= 14999.99:
        rate = .12
    elif sales >= 15000. and sales <= 17999.99:
        rate = .14
    elif sales >= 18000. and sales <= 21999.99:
        rate = .16

    else:
        rate = .18

    return rate

#call main function

main()