# this program uses a function to calculate the total of the values

def main():

    # create list

    numbers = [2,4,6,8,10]

    # display the total of the list elements

    print("The total is", get_total(numbers))

# the get_total function accepts a list as an argument returns the total of the
# values in the list


def get_total(value_list):

    # create a variable to use as an accumulator

    total = 0

    # calculate the total of the list elements

    for num in value_list:

        total = total + num
    # return the total

    return total

main()