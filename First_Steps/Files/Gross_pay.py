# this program displays gross pay

# get the number of hours worked

hours = int(input('Enter the hours worked this week: '))

# get the hourly rate

pay_rate = float(input('Enter the hourly pay rate'))

# calculate the gross pay

gross_pay = hours * pay_rate

#display the gross pay

print(f'Gross pay : $ {gross_pay:.2f}')
      