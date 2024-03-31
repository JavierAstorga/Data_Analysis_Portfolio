print('\n\n', '*'*40, '\n\n')


# ##Roman Numerals

# user_number = int(input('Please, enter a Interger number between 1 and 10: '))

# #Print the Roman Numeral

# if user_number == 1:

#     print('I')

# elif user_number == 2:

#     print('II')

# elif user_number == 3:
#     print('III')

# elif user_number == 4:
#     print('IV')

# elif user_number == 5:
#     print('V')

# elif user_number == 6:
#     print('VI')

# elif user_number == 7:
#     print('VII')

# elif user_number == 8:
#     print('VIII')

# elif user_number == 9:
#     print('IX')

# elif user_number == 10:
#     print('X')

# else:
#     print('Error: Invalid Number')




# #*******************************************************************************************


# #Question 3 

# # Mass and Weight

# print("Let's calculate an object weight with their mass. \n\n")

# obj_mass = float(input('Please, enter the object mass: '))

# weight = obj_mass *9.8

# print('The object mass is ', format(weight, '.2f'), 'newtons.')

# if weight > 500:
#     print('The object is too heavy.')

# elif weight < 100:
#     print('The object is too light.') 




# #********************************************************

# # Question 7

# # Grade Calculator

# print('Please enter the points for both tests and the exam. \n\n')

# test1 = int(input('Test 1 points: '))

# if not(0< test1 <25 ):
#     print('Error. Test scores must be between 0 and 25.')


# test2 = int(input('Test 2 points: '))

# if not(0< test2 <25):
#     print('Error. Test scores must be between 0 and 25.')


# exam = int(input('Exam points: '))

# if not(0< exam <50):
#     print('Error. Exam score must be between 0 and 50.')



# total_score = test1 + test2 + exam

# print('Your total score is: ', total_score, 'points')
# if total_score <50 or exam <25:
#     print('Grade : Fail')
# elif total_score < 80:
#     print('Grade: Distinction')
# elif total_score > 80 and total_score <= 60:
#     print('Grade: Credit')
# elif total_score <60 and total_score >50:
#     print('Grade: Pass')

##********************************************************************
# #Question 11

# #Book Club Points

# print("Let's check your points awarded.\n")

# user_points = 0

# books_pur = int(input('Please enter how many books have you purchase this month: '))

# if books_pur <2:
#     user_points += 0

# elif 2 <= books_pur <4:
#     user_points +=5

# elif 4<= books_pur <6:
#     user_points +=15

# elif 6<= books_pur <8:
#     user_points +=30

# elif 8<= books_pur:
#     user_points +=60

# print('Your points are: ', user_points, 'for purcharsing ', books_pur)


# #Question 12

# #Software Sales

# print("Let's check if you apply for a discount. \n\n")

# price = 99

# discount = 0

# quantity = int(input('Please enter the number of packages purchased: '))

# if quantity < 10:
#     discount = 0

# elif 10<= quantity <20:
#     discount =10

# elif 20<= quantity <50:
#     discount =20

# elif 50<= quantity <100:
#     discount =30

# elif quantity <=100:
#     discount =40

# total_pur = price * quantity

# total_discount = total_pur*(discount/100)

# total_final = total_pur - total_discount

# print('Your discount is ', discount,
#        '%. Which is: $', total_discount,
#        '\nAnd the total amount of the purchase after the discounts is: $',
#          total_final)



# #Question 13

# # Shipping charges

# # Get the weight of the package from the user
# weight = float(input("Please enter the weight of the package (in pounds): "))

# # Determine the shipping charges based on the weight
# if weight <= 2:
#     rate = 1.50
# elif weight <= 6:
#     rate = 3.00
# elif weight <= 10:
#     rate = 4.00
# else:
#     rate = 4.75

# # Calculate the total shipping charge
# charge = rate * weight

# # Display the shipping charges
# print(f"The shipping charges for a package weighing {weight} pounds is ${charge:.2f}.")




# #Question 14

# # Body Mass Index

# print('Please enter the following information --> ')

# weight = float(input('Weight: '))

# height = float(input('Height: '))


# bmi = weight * (703/height**2)


# print(f'\n\nYour BMI is {bmi:.2f}')

# if 18.5 <= bmi <= 25:
#     print('Your weight is Optimal')

# elif bmi < 18.5:
#     print('You are underweight')

# elif bmi > 25:
#     print('You are overweight')








# #Question 15

# # Time Calculator

# seconds = int(input('Number of Seconds: '))


# if seconds >= 86400:
#     days = seconds // 86400
#     seconds = seconds % 86400
#     hours = seconds // 3600
#     seconds = seconds % 3600
#     minutes = seconds // 60
#     seconds = seconds % 60
#     print(f'{days} day(s), {hours} hour(s), {minutes} minute(s), and {seconds} seconds')


# elif seconds >= 3600:
#     hours = seconds // 3600
#     seconds = seconds % 3600
#     minutes = seconds // 60
#     seconds = seconds % 60
#     print(f'{hours} hour(s), {minutes} minute(s), and {seconds} seconds')

# elif seconds >= 60:
#     minutes = seconds // 60
#     seconds = seconds % 60
#     print(f'{minutes} minute(s), and {seconds} seconds')

# else:
#     print(f'{seconds} second(s)')



# Question 17

# Wifi diagnostic test

print('Please always answer with just "Y" or "N" for Yes or No')

answer = input('Do you have bad WIFI connection? ')

if answer == 'Y':
    print('Reboot the computer and try to connect.')
    answer = input('Did that fix the problem? ')
    if answer == 'N':
        print('Reboot the rooter.')
        answer = input('Did that fix the problem? ')
        if answer == 'N':
            print('Make sure cables between router pc are plugged in firmly.')
            answer = input('Did that fix the problem? ')
            if answer == 'N':
                print('Move the router to a new location.')
                answer = input('Did that fix the problem? ')
                if answer == 'N':
                    print('Get a new Router.')
                else:
                    print('Thanks, program end.')
            else:
                    print('Thanks, program end.')    
        else:
                    print('Thanks, program end.')
    else:
                    print('Thanks, program end.')
else:
                    print('Thanks, program end.')