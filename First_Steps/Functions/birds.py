# this program demonstrates 2 functions that have 
#local varables with the same name

def main(): 

    # call the dublin function

    dublin()

    #call the cavan function

    cavan()

    print("The end")

#definition of the dublin function
# it creates a local variable named birds

def dublin():

    birds = 5000

    print('Dublin has', birds, 'Birds')

# definition of the Cavan function
# it creates a local variable called birds

def cavan():
    
    birds = 8000

    print('Cavan has', birds, 'birds')

#call the main function

main()