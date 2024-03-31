# this program allows the user to choose varius geometry
# calculations from a menu. This program imports the circle
# and rectangle modules which you just programmed.

# You must add these modules to this program
# how do you do this:
# Click on the program geometry in the solution on right
# hand side, then right click, click ad existing item.
# You must do this for curcle and rectangle modules.
# The solution you should see under geometru, circle.py 
# and rectangle.py

#we import out circle module which we just programmed

import circle
# we import rectanglel module which we just programmed

import rectangle

#constant Value for the menu choices

area_cirlce_choice = 1

circunference_choice = 2

area_rectangle_choice = 3

perimeter_rectangle_choice = 4

quit_choice = 5

#the main function

def main():

    #the choice variable controls the loop
    #and holds the user's menu
    choice = 0

    while choice != quit_choice:
        # display the menu

        display_menu()

        #get the user's choice

        choice = int(input('Enter choice: '))

        #perform the selected action

        if choice == area_cirlce_choice:

            radius = float(input('Enter Circle Radius: '))

            # The circle module that you produced has a function called
            # area. Pass this radius which the user has given you
            # to this function. And then return with the area

            print(f"The Area of cricle is: {circle.area(radius)}")

        elif choice == circunference_choice:

            radius = float(input('Enter Circle Raidus: '))

            print(f'Circunference is: {circle.circumference(radius)}')

        elif choice == area_rectangle_choice:
            width = float(input('Enter the rectangle Width: '))

            length = float(input('Enter the Rectangle Length: '))

            # The rectangle module that you produced has a function 
            # called area. Paas this width and lenght which the user has
            # given you to this function. 
            # Pas the width and lenght to the area function in the rectangle module

            print(f"The Area is: {rectangle.area(width, length)}")

        elif choice == perimeter_rectangle_choice:

            width = float(input('Enter the rectangle Width: '))

            length = float(input('Enter the Rectangle Length: '))

            print(f"The Perimeter is: {rectangle.perimeter(width, length)}")

        elif choice == quit_choice:
            print('Exit')

        else: 
            print('ERROR Invalid Selection')
    
        print('\n','-'*20)

# The display menu function displays the choice you wish to make


def display_menu():

    print('     MENU:\n1) Area of Circle\n2) Cricunference of Circle\n3) Area of Rectangle\n4) Perimeter of Rectangle\n5) Quit')


main()