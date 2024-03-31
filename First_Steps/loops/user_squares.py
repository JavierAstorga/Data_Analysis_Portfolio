#Get the ending limit

print('This program Displays a list of Numbers')

print('(Starting at 1) and their squares ')

end = int(input('How high do you want to go: '))

#print the table headings

print('\nNumber\tSquare\n','-'*12)

#print the numbers and their squares 

#end is the end value the user inputs plus 1. i.e. want to get number (1, end + 1) ---> (1,21)

for number in range(1, end + 1):

    square = number **2

    print(number, '\t', square)