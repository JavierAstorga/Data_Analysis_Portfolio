# this program displays a simple line graph

import matplotlib.pyplot as plt

def main():

    # create lists with the x and y coordinates of each data point

    x_coords = [0,1,2,3,4]

    y_coords = [0,3,1,5,2]

    # build the line graph
    plt.plot(x_coords,y_coords)

    # disyplay the line graph
    plt.show

# call the main function.

main()