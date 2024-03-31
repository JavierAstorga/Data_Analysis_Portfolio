# this program demonstrates what happens when you change the value of a parametewr

def main():
    value = 99

    print('The value is', value)

    #call the change_me function and pass the value to this function

    change_me(value)

    # when return from the change_me function we print the

    print('Back in main the value is ', value)


def change_me(arg):

    print('I am changing the value')

    arg = 0

    print('Now the value is: ', arg)

#call the main value
main()