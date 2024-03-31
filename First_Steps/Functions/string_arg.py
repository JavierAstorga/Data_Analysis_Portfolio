#THis program demostrates passing 2 string arguments to a function

def main():
    
    first_name = input('Enter your First name: ')

    last_name = input('Enter your Last name: ')

    print('Your name Reversed is')

    #call a function to reverse the name

    reverse_name(first_name,last_name)


#reverse function

def reverse_name(first,last):
    first = first[::-1]
    last = last[::-1]
    print(last,first)

#Call the main function
main()