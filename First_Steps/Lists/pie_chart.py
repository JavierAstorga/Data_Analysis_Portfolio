# simple pie chart 

import matplotlib.pyplot as plt

def main():

    # create a list value

    values = [20,60,80,40]
    
    # create a pie chart from values

    plt.pie(values)

    # display pie chart

    plt.show()

main()