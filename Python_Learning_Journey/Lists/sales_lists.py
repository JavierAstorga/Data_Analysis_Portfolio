# the NUM_DAYS constant hold the number of days that we will gather sales data for

num_days = 5

def main():

    # create a list to hold the sales for each day

    sales = [0] * num_days

    # create a variable to hold the index

    index = 0

    print('Enter the sales for each Day: ')

    # get the sales for each day
    # Populate the list

    while index < num_days:

        print(f'Day # {index + 1}: ', end= '')      # end='' DO NOT GO TO NEW LINE

        sales[index] = float(input())

        index = index + 1

    # display the values entered into the list


    print('Here are the values you entered')

    for value in sales:

        print(value)

# call main funtcion
main()      