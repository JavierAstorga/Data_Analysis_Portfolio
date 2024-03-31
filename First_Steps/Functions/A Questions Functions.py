print('\n\n','*'*30,'\n\n')



# #Question 1       ****************************************************


# input_user = 30
# # input_user = 400
# # input_user = 1
# # input_user = 4000


# def main():
#     distance_user = input_user

#     kmtomiles(distance_user)


# def kmtomiles(km):
#     miles = km * 0.6214

#     print(f'You drive {km} km, and that is {miles:.2f} miles')

# main()



# #Question 2       ****************************************************

# input_string = 'messi'
# input_int = 3
# # input_string = 'Hi'
# # input_int = 3
# # input_string = ''
# # input_int = 

# def main():
#     string = input_string

#     integer = input_int

#     repeat(string,integer)

# def repeat(string,integer):
#     repeater = string*integer
#     print(repeater)

# main()


# #Question 3   *******************************************************

# def main():

#     cost_build = float(input('Enter how much it will cost to replace the building? : $'))

#     insurance(cost_build)

# def insurance(val1):
#     amount_ins = val1 * 0.80

#     print(f'The minimun amount of insurance of the building will be ${amount_ins}')

# main()


# # #Question 4   **************************************************

# def main():
#     print('I will ask you the monthly cost of the next expenses of your automobile')
#     print('Please enter the costs next to each item.\n')
    
#     print('Expense\t\t\tCost\n','-'*30)

#     car_expenses()


# def car_expenses():

#     expenses = {}
#     items = ['Loan Payment', 'Insurance', 'Gas\t', 'Oil\t', 'Tires\t', 'Maintenance']


#     for i in items:
#         cost = input(f'{i}\t\t$')
#         expenses[i] = float(cost)
#         print('-'*30)

#     total_cost = sum(expenses.values())
#     print(f'Total Month\t\t${total_cost:.2f}\n')
#     print(f'Total Year\t\t${(total_cost)*12:.2f}')

# main()


# # Question 5 ***********************************************

# def main():
#     property_val = float(input('Please enter the actual value of the property: $'))

#     cal_property_tax(property_val)





# def cal_property_tax(val1):

#     assessment = val1 * .60    

#     tax = assessment * 0.072

#     print(f'The assessment value is : ${assessment:.2f}\nAnd the property tax is : ${tax:.2f}')


# main()


# # Question 13        ******************************************************

# def main():
#     g = 9.8

#     print('Time\t\t Distance Falling')
#     print('-'*30)
#     d = 0.0
#     t = int(input('How many SECONDS the object is falling?: '))

#     falling_distance(g,d,t)

# def falling_distance(g,d,t):
#     for sec in range(1,11):
#         d += 0.5*g*(t**2)
#         print(f'{int(t*(sec/10))} seconds\t {d:.2f} meters')

# main()


# Question 14

def main():

    m = float(input('Mass of the object in KG: '))

    v = float(input('Velocity of the object in m/s: '))

    ke = cal_ke(m,v)

    print(f'Your Kenectic Energy is {ke}')

def cal_ke(m,v):
    KE = 0.5*m*(v**2)
    return KE


main()