

import matplotlib.pyplot as plt

def main():

    # create list of sales amount

    sales = [100,200,300,400]

    # create a list of labels for the slices

    slice_labels = ['1st Qrt','2nd Qrt','3rd Qtr','4th Qrt']

    # create a pie chart from the values

    plt.pie(sales, labels =slice_labels)

    # add title 
    plt.title('Sales by Quarter')

    plt.show()

main()