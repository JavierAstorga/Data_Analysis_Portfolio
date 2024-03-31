#This program averages test scores. It askis the user for the number of students and
# the number of test score per student

#Get the number of students

num_students = int(input('Enter How many students do you have: '))

#Get the number of test scores per student

num_test_scores = int(input('How Many test scores per student: '))

#Determine each students average test score

for student in range(num_students):     # outer loop does this first

    # Initialize an Accumulator for test scores

    total = 0.0

    #Get the student's test scores

    print(f'Student Number {student + 1}')      #student = 1 reason for this is that range
                                                # from 0 upwards.
    print('-'*20)

    for test_num in range(num_test_scores):     #inner loop

        print(f'Test Number {test_num + 1}')

        score = float(input(':'))


        #Add the score to the accumulator

        total = total + score

    #calculate the average test score for this student

    average = total / num_test_scores

    #Display the average

    print(f'The average for student Number {student + 1} is {average:.1f}')