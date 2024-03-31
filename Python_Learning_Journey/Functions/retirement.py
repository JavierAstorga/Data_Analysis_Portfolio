#The following program is used as a global constant to represent
#the contribuition rate

contribution_rate = 0.05

def main():
    gross_pay = float(input('Enter the gross pay: '))

    bonus = float(input('Enter the amount of Bonuses'))

    #Function called show_pay_contrib which 
    #passes the gross_pay to this function

    show_pay_contrib(gross_pay)

    #Function called show_bonus_contrib which passes the
    #bonus to this function

    show_bonus_contrib(bonus)

#The show pay contrib function accepts the gross pay as an
# argument and displays the retirement 
# contribution for that amount of pay


def show_pay_contrib(gross):    # the gross variable stores 
                                # the gross_pay that the user 
                                # just entered
    contrib = gross * contribution_rate

    print(f'Contribution for gross pay: ${contrib:.2f}')


def show_bonus_contrib(bonus):
    contrib = bonus * contribution_rate

    print(f'Contribution for bonuses: ${contrib:.2f}')

#call the main function

main()