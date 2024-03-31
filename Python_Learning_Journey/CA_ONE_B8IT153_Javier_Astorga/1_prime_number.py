
# Prime Number Checker

# This program checks if a given number is prime.
# The user enters a number, and the program determines whether it is prime or not.?
# It uses an efficient method of checking for factors up to the square root of the number.
   
def main():
    try:
        # The 'try' block is used to attempt the execution of code that might raise an error.
        # In this case, it is used to handle cases where the input is not an integer.
        number = int(input("Enter a number: "))

        # This 'if' statement checks if the entered number is less than 2.
        # Since prime numbers are greater than 1, this condition ensures that only valid numbers are checked for primality.
        # Prime Number: must have only two positive factors. For 1, the number of positive divisors or factors is only one.
        if number < 2:
            print("Please enter an integer greater than 1.")
        
        # The 'elif' here checks specifically if the number is 2.
        # Since 2 is the only even prime number, it's treated as a special case.
        elif number == 2:
            print(f'{number} is a prime number')
        
        else:
            # The 'for' loop here checks for factors of the number.
            # The range goes from 2 to the square root of the number, incremented by 1.
            # Mathematically, if a number is not prime, it must have a factor less than or equal to its square root.
            # This is because any factors of n will be pairs (a, b) where a * b = n.
            # If both a and b were greater than the square root of n, then a * b would be more than n (impossible).
            # Thus, checking up to the square root of n is sufficient.
            for i in range(2, int(number**0.5) + 1):
                # If the number is divisible by any number in the range, it's not prime.
                if number % i == 0:
                    print(f"{number} is not a prime number.")
                    break  # This 'break' exits the loop as soon as a factor is found.
            
            else:
                # The 'else' block here is part of the 'for' loop (not the 'if' statement).
                # It executes only if the loop completes without finding any factors, indicating that the number is prime.
                print(f'{number} is a prime number')

    except ValueError:
        # The 'except' block catches the ValueError that occurs if the input cannot be converted to an integer.
        # This is necessary to handle inputs like strings or floats, which aren't valid integers.
        print("Please enter a valid integer.")

# Call the main function to run the program.
main()




# 4397
# 10631
# 648391
# 4535189
# 250751
# 4952019383323
# 53982894593057