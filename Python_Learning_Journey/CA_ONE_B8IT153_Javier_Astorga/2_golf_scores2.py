# 2. Display Records: This part of the program reads the records from 'golf.txt' and displays them.
# It's intended to provide an easy way to review all players' scores from the tournament.


# Program 2: Reading and Displaying Records from golf.txt

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


# Call the main function to run the program.
main()