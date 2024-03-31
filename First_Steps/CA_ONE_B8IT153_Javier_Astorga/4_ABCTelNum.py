# Alphabetic Telephone Number Translator
# This program converts a telephone number with alphabetic characters into its numeric equivalent.
# The user is prompted to enter a 10-character telephone number in the format XXX-XXX-XXXX.
# The program then translates any alphabetic characters into their corresponding numbers as per standard telephone keypad mapping.


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

    
    # Remove hyphens from the input
    # This step ensures that the program can process phone numbers entered with or without hyphens,
    # making it more flexible and user-friendly.
    user_input = user_input.replace('-', '')

    
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

# Call the main function to run the program.
main()




# 646-SAY-YES1
# 408-BUY-TECH
# 305-SUN-POOL
# 202-WIN-SALE
# 617-FLY-AWAY
# 323-FUN-TOYS
# 714-NEW-HOME
# 505-GET-HELP