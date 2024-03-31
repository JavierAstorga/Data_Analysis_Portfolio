# this program gets a serires of test scores and calculates the average of the scores with the lowest score dropped

def main():

    # get the test Scores from the user

    scores = get_scores()

    # get the total of the test scores

    total = get_total(scores)

    # get the lowest test scores

    lowest = min(scores)

    # substract the lowest score from the total

    total = total - lowest

    # calcualate the average. Note that we divide by 1 less than the number of scores because the lowest scires was dropped

    average = total / (len(scores) - 1)

    # display the average

    print(f' the Average, with the lowest score Dropped is : {average:.2f}')

# the get_scores function gets a series of test scores from the user and stores them in a list
# a reference to the list is returned


def get_scores():

    # create an empty list

    test_scores = []

    # create variable control loop

    again = 'y'

    # get the scores from the user and add them to the list

    while again == 'y': 

        # get score and add it to the list

        value = float(input('Enter a test score: '))


        test_scores.append(value)

        # do you want to go again

        print('Do you want to add another score: ')

        again = input('y = yes, anythign else = no')

    # returns with list

    return test_scores

# the function get_total accpets a list as an argument
# returns the total of the values in the list

def get_total(value_list):

    # create a variable to use as accumulator

    total = 0.0

    # calculate the total of the list elements

    for num in value_list:

        total = total + num
    
    return total

main()