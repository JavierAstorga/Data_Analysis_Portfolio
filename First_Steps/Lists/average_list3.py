def main():

    # create a list

    scores = [2.5, 7.3, 6.5, 4.0, 5.2]

    # creates a variable to use as an accumulator 

    total = 0.0

    # calculate the total of the list elements

    for value in scores:

        total = total + value

    # calculate the average of the elements

    average = total /len(scores)

    # diasplay the total of the list elements

    print('The Average of the Element is ', average)

main()