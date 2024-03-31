print('\n\n','*'*30,'\n\n')


# Assume a file contains a series of numbers integers named numbers.txt exists
# on your disk. Write a program that displays all the numbers in the file

# def main():

#     file = open(r'C:\Users\javie\Downloads\College\Programing projects\Files\Numbers.txt', 'r')

#     for line in file:

#         number = line.strip()

#         print(number)

#     # Lecture code:

#         # contents = ''

#         # file = open(r'C:\Users\javie\Downloads\College\Programing projects\Files\Numbers.txt', 'r')

#         # contents = file.read()

#         # file.close()
#         # print(contents)

# main()

##Question 2 File Head Display

# def main():

#     file_name = input('What is the name of the file? : ')

#     file = open(r'C:\Users\javie\Downloads\College\Programing projects\Files\\' + file_name, 'r')

#     for line in file:

#         textline = line.strip()

#         print(textline)



#     #Another Alternative:

#     # contentline = ''
#     # contentline = file.read()
#     # file.close()
#     # print(contentline)

#     #Lecture Alternative:

#     # line = ''

#     # counter = 0

#     # filename = input('Enter the Name of the File: ')

#     # infile = open ...

#     # line = infile.readline()

#     # counter = 1

#     # while line != '' and counter <= 5:

#     #     line = line.rstrip('\n')
#     #     print(line)
#     #     line = infile.readline()
#     #     counter = counter + 1
#     # infile.close()

# main()


# #Question 3   Line Numbers

# def main():

#     file_name = input('What is the name of the file? : ')

#     file = open(r'C:\Users\javie\Downloads\College\Programing projects\Files\\' + file_name, 'r')

#     counter = 0

#     for line in file:

#         textline = line.strip()

#         counter += 1

#         print(f'{counter}: {textline}')

# main()


# Question 4    High Score


# def main():
# #     score_file = open(r'C:\Users\javie\Downloads\College\Programing projects\questions_files\scores.txt', 'w')

# #     score_content = """John Doe, 87
# # Jane Smith, 93
# # Bob Johnson, 78
# # Alice Brown, 95
# # Tom Clark, 82"""

# #     score_file.write(score_content)

# #     score_file.close()

# #     print('score file created')

#     read_content = open(r'C:\Users\javie\Downloads\College\Programing projects\questions_files\scores.txt', 'r')

#     high_score = 0
#     high_score_name = ''
#     record_count = 0

#     for line in read_content:

#         record_count +=1

#         name, score = line.strip().split(', ')


#         score = int(score)

#         if score > high_score:
#             high_score = score
#             high_score_name = name

#     print('This is the highest value')
#     print(f'Subject: {high_score_name}, Score: {high_score} , Record Count: {record_count}')

# main()


# # Question 5    Sum of Numbers

# def main():

#     rfile = open(r'C:\Users\javie\Downloads\College\Programing projects\Files\Numbers.txt', 'r')

#     numbers = []

#     for value in rfile:

#         value_strip = int(value.rstrip('\n'))

#         if value:
#                 value_strip = int(value)
#                 numbers.append(value_strip)

#         print(numbers)

#     total = sum(numbers)  
#     print('The total is : ', total)

# main()

##########################################################

# #   Question 6 Average Numbers

# def main():

#     rfile = open(r'C:\Users\javie\Downloads\College\Programing projects\Files\Numbers.txt', 'r')

#     numbers = []

#     for value in rfile:

#         value_strip = int(value.rstrip('\n'))

#         if value:
#                 value_strip = int(value)
#                 numbers.append(value_strip)

#         print(numbers)

#     total = sum(numbers)  

#     count = len(numbers)

#     average = total / count


#     print('The total is : ', total)

#     print(f"The average is: {average:.2f}")

    

# main()


###################################################

# # Question 7

# def main():
#     amount_words = int(input('How many words you want to write: '))

#     words = []

#     outfile = open(r'C:\Users\javie\Downloads\College\Programing projects\questions_files\words.txt', 'w')

#     for i in range(amount_words +1):

#         word = input('Enter the word you want to write one at a time: ')
#         outfile.write(word + '\n')

#     outfile.close()




# main()


#########################################################################

# # Question 1

# # valid Number  Information


# numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]

# valid_numbers = []

# for i in numbers:
#     if 0 <= i <= 100:
#         valid_numbers.append(i)


# total = sum(valid_numbers)

# average = total / len(valid_numbers)

# print('Valid number: ', valid_numbers)

# print('Total: ', total)

# print('Average: ', format(average,'.2f'))


##########################################

# # Question 2

# # Lottery Number Generator

# import random

# lottery_num = []

# for i in range(7):

#     number = random.randint(0, 9)
#     lottery_num.append(number)

# print("Lottery Numbers:", end=" ", )
# for number in lottery_num:
#     print(number, end=" ")


################################

# # question 3

# # Rainfall Statistics

# month_rainfall = []

# for value in range(1,13):

#     rainfall = float(input(f' Enter the rainfall of the month {value}: '))

#     month_rainfall.append(rainfall)

# total_rainfall = sum(month_rainfall)

# average_rf = total_rainfall / 12

# max_rf = max(month_rainfall)

# min_rf = min(month_rainfall)

# max_month = month_rainfall.index(max_rf) + 1

# min_month = month_rainfall.index(min_rf) + 1

# print(f'\nThe total rainfall over the year is {total_rainfall:.2f}')

# print(f'\nThe average rainfall of the year is {average_rf:.2f}')

# print(f'\nThe month with most rainfall is the {max_month} month with {max_rf:.2f} rainfall')

# print(f'\nThe most with lowest rainfall is the {min_month} month with {min_rf:.2f} rainfall')





###########################################################

# # Question 4

# numbers = []

# print('Please Enter 20 Numbers:')


# for i in range(1,21):
#     number = float(input(f'Number {i} :'))
#     numbers.append(number)


# lowest_number = min(numbers)
# highest_number = max(numbers)
# total = sum(numbers)
# average = total / len(numbers)


# print(f"The lowest number in the list is {lowest_number}.")
# print(f"The highest number in the list is {highest_number}.")
# print(f"The total of the numbers in the list is {total}.")
# print(f"The average of the numbers in the list is {average:.2f}.")




#########################


# Question 5

# Charge Account Validation


# Function to read account numbers from a file and return them as a list
def read_account_numbers(file_path):
    with open(file_path, 'r') as file:
        # Read each line in the file and strip any newline characters
        accounts = [line.strip() for line in file]
    return accounts

# Main program
def main():
    # Read the list of valid account numbers from the file
    valid_accounts = read_account_numbers('charge_accounts.txt')
    
    # Ask the user for an account number
    user_account = input("Please enter a charge account number: ")
    
    # Check if the entered account number is valid
    if user_account in valid_accounts:
        print("The number is valid.")
    else:
        print("The number is invalid.")

# Run the program
main()
