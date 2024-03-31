# This program assists a technitian in the process
#of checking a substance's temperture

#Create a variable to represent the Maximun Temperture

max_temp = 102.5

#Get the substance's temperture

temperture = float(input('Enter the substances Temperture in Celcius: '))

#As long as the necesary instruct the user to 
#adjust the termostat

while temperture > max_temp:
  #When the while loop is true it executes the following statement

    print('The temperture is too high')

    print('Turn the termostat Down and Wait')

    print('5 minutes. Then take the temperture\nAgain and Enter it')

    temperture = float(input('Enter the New celcius tempeture: '))

 # Remind the user to check the tempeture again
 #in 15 minutes
 # These statement is execute when the while loop is false

print('The temperture is acceptable')

print('Check it again in 15 minutes')