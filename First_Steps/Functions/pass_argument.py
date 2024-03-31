
#pased to a function

def main():
    value = 5

    show_double(value) #pass the value [which is 5] to
                        #Function show_double()

# the show_double function accepts an argument
# and displays double its value

def show_double(number):    #number now has a copy of the
                            #the value which is 5

    result = number * 2

    print(result)

# call the main function

main()
