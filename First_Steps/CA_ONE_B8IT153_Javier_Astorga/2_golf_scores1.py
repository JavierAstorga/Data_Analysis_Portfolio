# Golf Scores Management System
# This program is designed for the DBS Amateur Golf Club to manage their tournament scores. It consists of two main functionalities:
# 1. Input Handler: It allows for the input of each player's name and golf score through keyboard input. 
# This information is then stored in a file named 'golf.txt'. Each record in the file includes fields for the player's name and their score.

# The program is structured to ensure ease of use and efficient data handling for the club's weekend tournaments.


# Program 1: Writing Player Names and Scores to golf.txt

def main():
    # Open the file "golf.txt" for appending.
    #  'a' mode is used to add new data to the end of the file without deleting existing data.
    golf_file = open(r'C:\Users\javie\Downloads\College\Programing projects\Assessment\golf1.txt', 'a')    
    
    while True:         # A while loop with condition True will continue indefinitely until it is explicitly broken.
        # Get player's name. The input function is used to receive user input from the console.
        player_name = input("Enter player's name (or type 'exit' to stop): ")
        # Check if the user wants to exit the loop. Lower() is used to make the comparison case-insensitive.
        if player_name.lower() == 'exit':
            break           # The break statement exits the nearest enclosing loop, in this case, the while loop.

        # Get player's score as input from the user.
        player_score = input("Enter player's score: ")

        # Write the player's name and score to the file, followed by a newline character.
        golf_file.write(f"{player_name},{player_score}\n")

        # Print a confirmation message to the console.
        print(f"Record added for {player_name}")

# Call the main function to run the program.
main()


# Alice,72
# Bob,68
# David,74
# Dana,70
# Ethan,69
# Fiona,67
# George,75
# Hannah,71
# Ian,73
# Julia,66