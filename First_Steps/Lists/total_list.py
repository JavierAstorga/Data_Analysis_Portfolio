# this program calculates the total of the values in a list

def main():

    # create your list

    numbers = [2,4,6,8,10]

    # create a variable to use as an accumulator

    total = 0

    # calcualte the total of the list elements

    for value in numbers:

        total = total + value

    # display the total of the list elements

    print('The total of the elements is' , total)

main()