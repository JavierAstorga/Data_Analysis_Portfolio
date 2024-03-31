# This program calculates a retail items sale price 
# Discount percentage 20%

discount_percent = .2

def main():
    #get the items regular price 
    # go to the function get_regular_price and return with the 
    # regular price

    reg_price = get_regular_price()

    #the sales price

    #go to the discount function and bring the reg_price to 
    #this function. It will return the discount which
    #will then be subsstraced from reg_price

    sale_price = reg_price - discount(reg_price)

    #display the sales price

    print(f'The sales price is: $ {sale_price:.2f}')

#the get_regular_price function prompts the user to enter
# an items regular price and it returns that value to reg_price

def get_regular_price():

    price = float(input('Enter the Items regular price: '))

    return price

#the discount function accepts an items price as an argumnt 
# and returns the amount of discount

def discount(price):

    return price* discount_percent

main()