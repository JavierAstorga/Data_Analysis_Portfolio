# simple line graph

import matplotlib as plt

def main():

    # create x and y coords

    x_coords = [0,1,2,3,4]

    y_coords = [0,3,1,5,1]

    # build line graph

    plt.plot(x_coords,y_coords)

    # add title

    plt.title('Simple data')

    # add labels to axis

    plt.xlabel('This is x axis')

    plt.ylabel('This is the y axis')