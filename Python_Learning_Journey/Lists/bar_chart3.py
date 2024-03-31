# this program displys a Sales chart

import matplotlib.pyplot as plt

def main():

    # create a list with X coordinates of each Bar's left edge

    left_edge = [0,10,20,30,40]
    
    # create a list with the heights of each bar

    heights = [100,200,300,400,500]

    bar_width = 10

    # build the bar chart

    plt.bar(left_edge, heights, bar_width, color = ('r','g','b','y','k'))

    # add title

    plt.title('Sales by Year')

    # add labels to the axes

    plt.xlabel('Year')

    plt.ylabel('Sales')

    # customize the ticks marks

    plt.xticks([5,15,25,35,45],

        ['2016','2017','2018','2019','2020'])
    
    plt.yticks([0,100,200,300,400,500],
               ['$0m', '$1m','$2m','$3m','$4m','$5m'])
    
    # display the chart

    plt.show()

main()