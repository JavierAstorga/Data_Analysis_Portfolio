# simple bar chart, with width 

import matplotlib.pyplot as plt

def main():

    # create a list with X coordinates of each Bar's left edge

    left_edge = [0,10,20,30,40]
    
    # create a list with the heights of each bar

    heights = [100,200,300,400,500]

    bar_width = 5

    # build the bar chart

    plt.bar(left_edge, heights, bar_width)

    # display chart

    plt.show()

main()