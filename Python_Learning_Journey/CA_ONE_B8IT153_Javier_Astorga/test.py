def main():
    try:
        number = int(input("Enter a number: "))

        if number < 2:
            print("Please enter an integer greater than 1.")
        elif number == 2:
            print(f'{number} is a prime number')
        else:
            # Square root method in prime number check
            # If a number n is not prime, it must have a divisor less than or equal to its square root.
            # This is because any factors of n will be pairs (a, b) where a * b = n.
            # If both a and b were greater than the square root of n, then a * b would be more than n (impossible).
            # Thus, checking up to the square root of n is sufficient.
            for i in range(2, int(number**0.5) + 1):
                if number % i == 0:
                    print(f"{number} is not a prime number.")
                    break
            else:
                print(f'{number} is a prime number')

    except ValueError:
        print("Please enter a valid integer.")

main()






def main():
    # Open the file "golf.txt" for appending. 'a' mode is used to add new data to the end of the file without deleting existing data.
    golf_file = open(r'C:\Users\javie\Downloads\College\Programing projects\Assessment\golf.txt', 'a')    
    
    while True: # A while loop with condition True will continue indefinitely until it is explicitly broken.
        # Get player's name. The input function is used to receive user input from the console.
        player_name = input("Enter player's name (or type 'exit' to stop): ")
        # Check if the user wants to exit the loop. Lower() is used to make the comparison case-insensitive.
        if player_name.lower() == 'exit':
            break # The break statement exits the nearest enclosing loop, in this case, the while loop.

        # Get player's score as input from the user.
        player_score = input("Enter player's score: ")

        # Write the player's name and score to the file, followed by a newline character.
        golf_file.write(f"{player_name},{player_score}\n")

        # Print a confirmation message to the console.
        print(f"Record added for {player_name}")

# Call the main function to run the program.
main()







def main():
    # Opening the file in read mode. The 'r' stands for "read". 
    # It means the file is opened for reading and no writing can be done to it.
    golf_file = open(r'C:\Users\javie\Downloads\College\Programing projects\Assessment\golf.txt', 'r') 

    # readlines() reads all the lines in the file and returns them as a list.
    # Each element in the list is one line from the file.
    # This is used instead of readline() (which reads just one line) or read() 
    # (which reads the entire file into a single string) because we want to process each line separately.
    lines = golf_file.readlines()

    # Printing the header for the output, for clarity and presentation.
    print("Golf Tournament Scores:")
    print("-----------------------")

    # The for loop iterates over each line in the list 'lines'.
    for i in lines:
        # strip() removes any leading or trailing whitespaces (including newline characters) from the line.
        # split(',') splits the line into a list at every comma. 
        # This is assuming each line in the file has the format "name,score".
        player_name, player_score = i.strip().split(',')

        # Printing the details of each player and their score.
        # This format ensures a consistent and readable output.
        print(f"Player: {player_name}, Score: {player_score}")    

main()




# This script reads expense data from a text file and plots a pie chart
# showing the distribution of expenses in various categories using matplotlib.

import matplotlib.pyplot as plt

# Function to read data from a text file and return a dictionary of expenses
def read_expenses(file_path):
    expenses = {}
    with open(file_path, 'r') as file:
        for line in file:
            category, amount = line.strip().split(',')
            expenses[category] = expenses.get(category, 0) + float(amount)
    return expenses

# Path to the text file containing expenses
file_path = 'expenses.txt'

# Reading the expenses data
expenses_data = read_expenses(file_path)

# Extracting categories and their corresponding amounts
categories = list(expenses_data.keys())
amounts = list(expenses_data.values())

# Plotting the pie chart
plt.figure(figsize=(8, 8))
plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
plt.title('Monthly Expense Distribution')
plt.show()







# Import the matplotlib.pyplot library
import matplotlib.pyplot as plt
# matplotlib.pyplot is a collection of command style functions that make matplotlib work like MATLAB. 
# It provides a state-based interface to plotting functions.

def main():
    # Initialize a dictionary to store expenses
    expenses = {}
    # A dictionary is used here because it allows for easy mapping of categories to their respective amounts.
    # The key-value pair structure is ideal for this kind of data.

    # Open the file containing expense data
    exp_file = open(r'C:\Users\javie\Downloads\College\Programing projects\Assessment\expenses.txt', 'r')
    # The 'open' function is used to read from a file. Here, the file path is specified along with 'r', 
    # which means the file is opened in "read" mode.

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
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
    # 'plt.figure' sets the figure size.
    # 'plt.pie' creates a pie chart with the amounts, labels for each category, 
    # percentage formatting, and a starting angle for the first segment.

    # Set the title of the plot
    plt.title('Monthly Expense Distribution')
    # 'plt.title' adds a title to the plot.

    # Display the plot
    plt.show()
    # 'plt.show' renders the plot to the screen.

# Call the main function to execute the program
main()





# Alphabetic Telephone Number Translator
# This program converts a telephone number with alphabetic characters into its numeric equivalent.
# The user is prompted to enter a 10-character telephone number in the format XXX-XXX-XXXX.
# The program then translates any alphabetic characters into their corresponding numbers as per standard telephone keypad mapping.

def translate_to_numeric(phone_number):
    # Mapping of alphabetic characters to numbers
    mapping = {
        'A': '2', 'B': '2', 'C': '2', 
        'D': '3', 'E': '3', 'F': '3',
        'G': '4', 'H': '4', 'I': '4',
        'J': '5', 'K': '5', 'L': '5',
        'M': '6', 'N': '6', 'O': '6',
        'P': '7', 'Q': '7', 'R': '7',
        'S': '7', 'T': '8', 'U': '8', 
        'V': '8', 'W': '9', 'X': '9',
        'Y': '9', 'Z': '9'
    }

    # Translate alphabetic characters to numeric
    numeric_phone_number = ""
    for char in phone_number:
        if char.isalpha():
            numeric_phone_number += mapping[char.upper()]
        else:
            numeric_phone_number += char

    return numeric_phone_number

# Main function to get user input and display the result
def main():
    user_input = input("Enter a 10-character telephone number (XXX-XXX-XXXX): ")
    translated_number = translate_to_numeric(user_input)
    print("Numeric telephone number:", translated_number)




def main():
    # Mapping dictionary: Maps alphabetic characters to their corresponding numeric values 
    # as per a standard telephone keypad. This makes it easy to translate each letter to a number.
    mapping = {
        'A': '2', 'B': '2', 'C': '2', 
        'D': '3', 'E': '3', 'F': '3',
        'G': '4', 'H': '4', 'I': '4',
        'J': '5', 'K': '5', 'L': '5',
        'M': '6', 'N': '6', 'O': '6',
        'P': '7', 'Q': '7', 'R': '7',
        'S': '7', 'T': '8', 'U': '8', 
        'V': '8', 'W': '9', 'X': '9',
        'Y': '9', 'Z': '9'
    }

    # User input: Prompting the user to enter a telephone number in a specific format.
    # This is the raw input that will be processed.
    user_input = input("Enter a 10-character telephone number (XXX-XXX-XXXX): ")

    # Initialization of the variable to store the numeric version of the phone number.
    numeric_pnumber = ''

    # Loop through each character in the user input.
    # If the character is in the mapping dictionary, replace it with the corresponding number.
    # Otherwise, keep the character as it is (useful for hyphens and numbers).
    for char in user_input:
        if char.upper() in mapping:
            numeric_pnumber += mapping[char.upper()]
        else:
            numeric_pnumber += char

    # Formatting the output: Converts the numeric phone number into the desired format (XXX-XXX-XXXX).
    # This makes the output consistent and easier to read.
    formatted_number = numeric_pnumber[:3] + '-' + numeric_pnumber[3:6] + '-' + numeric_pnumber[6:]
    
    # Printing the final result: Displays the translated and formatted telephone number.
    print("Numeric telephone number:", formatted_number)

# Invoking the main function to run the program.
main()
