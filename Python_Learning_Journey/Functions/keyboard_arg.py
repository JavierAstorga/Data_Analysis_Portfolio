#this program demonstrates keyword arguments

def main():
    
    #show the amount of simple interest using .01 as the interest
    #rate per period., 10 as the number of period
    #10,000 as the principal

    #CALL the function and pass the values above

    show_interest(rate=.01, periods=10, principal=10000.0)


#The show_interest function displays the amount of simple
#interest for a given period, principal and rate
def show_interest(principal, rate, periods):

    interest = principal * rate * periods

    print(f'The simple interest will be ${interest:.2f}')
          
#Call the main function
          
main()