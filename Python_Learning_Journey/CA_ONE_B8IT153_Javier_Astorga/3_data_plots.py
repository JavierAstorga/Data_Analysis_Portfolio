# The task involves two main steps:
# 1. Writing a text file ('expenses.txt') containing the expense data in various categories.
# 2. Developing a Python script to read this text file and plot the data in a pie chart using matplotlib.


# This script reads expense data from a text file and plots a pie chart
# showing the distribution of expenses in various categories using matplotlib.


# Import the matplotlib.pyplot library
# matplotlib.pyplot is a collection of command style functions that make matplotlib work like MATLAB. 
# It provides a state-based interface to plotting functions.
import matplotlib.pyplot as plt

def main():
    # Initialize a dictionary to store expenses
    expenses = {}
    # A dictionary is used here because it allows for easy mapping of categories to their respective amounts.
    # The key-value pair structure is ideal for this kind of data.

    
    # Open the file containing expense data
    exp_file = open(r'C:\Users\javie\Downloads\College\Programing projects\Assessment\expenses.txt', 'r')

    
    # Iterate over each line in the file
    for i in exp_file:
        # Split the line into category and amount, removing any leading/trailing whitespace
        category, amount = i.strip().split(',')
        # The 'strip' method removes any whitespace from the beginning and end of the string (i.e., each line).
        # The 'split' method then splits the line into parts at the comma, 
        # resulting in two parts: category and amount.

        # Update the expenses dictionary with the category and amount
        expenses[category] = expenses.get(category, 0) + float(amount)
        # This line adds the amount to the category key in the dictionary.
        # 'expenses.get(category, 0)' gets the current total for the category, 
        # or 0 if the category doesn't exist yet.
        # 'float(amount)' converts the amount string to a float for numerical operations.


    # Extract the categories and corresponding amounts as lists
    categories = list(expenses.keys())
    amounts = list(expenses.values())
    # The 'keys' method gets all the category names, and 'values' gets their corresponding amounts.
    # These are converted to lists for plotting purposes.


    # Plotting the expenses in a pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=90)
    # 'plt.figure' sets the figure size.
    # 'plt.pie' creates a pie chart with the amounts, labels for each category, 
    # percentage formatting, and a starting angle for the first segment.

    # Set the title of the plot
    plt.title('Monthly Expense Distribution')
    # 'plt.title' adds a title to the plot.

    plt.show()
    # 'plt.show' renders the plot to the screen.


# Call the main function to run the program.
main()