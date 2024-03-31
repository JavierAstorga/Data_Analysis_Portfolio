# this program uses the return value of a function

def main():

    #get the user's age

    first_age = int(input('Enter your age: '))

    #Get the user's best friends age

    second_age = int(input("Enter your friend's age: "))

    #get the sum of both ages 

    total = sum(first_age, second_age)

    #display the total ages

    print('Together you are', total, 'Years old')

    #The sum function accepts 2 numeric arguments and returns the sum of those arguments

def sum(num1, num2):

    result  = num1 + num2

    return result
    
#call main

main()