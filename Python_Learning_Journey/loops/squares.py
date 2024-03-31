#This program uses a loop to display a 
#table showing the numbers 1 through to 10
#and their squares

#Print the headings

print('Number\tSquare')

print('_'*10)

#print number 1 throught to 10
#and their squares

for number in range(1,11): #For loop starting at 1 and ending at 10

    square = number **2

    print(number,'\t',square)