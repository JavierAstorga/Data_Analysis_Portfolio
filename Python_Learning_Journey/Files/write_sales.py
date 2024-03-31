#This program prompts the user for sales amounts
# and writes those amounts to the sale.txt file

def main():
    num_days = int(input('For how many days do you have sales?: '))

    sales_file = open(r'C:\Users\javie\Downloads\College\Programing projects\Files\Sales.txt', 'w')

    # Range goes from 0 to n-1
    #  Say num_days = 3 ---> 0, 1, 2
    #  Want to start at 1 and end at 3

    for count in range(1,num_days + 1):

        sales = float(input('Enter the sales for Day #: ' + str(count) + ':'))
        #You have to convert the sales figure given by user to a string
        #  Reason is that it is written out to file as string

        sales_file.write(str(sales) + '\n')

        #For loop is finished

    sales_file.close()

    print('Data Written')

main()