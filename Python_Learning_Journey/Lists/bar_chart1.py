# this program displays a simple bar chart

import matplotlib.pyplot as plt

def main():

    # create a list with X coordinates of each bar's left edge

    left_edge = [0,10,20,30,40]

    # create a list with the weights of each bar

    heigts = [100,200,300,400,500]

    # build the bar chart

    plt.bar(left_edge, heigts)

    # display bar chart

    plt.show()

main()