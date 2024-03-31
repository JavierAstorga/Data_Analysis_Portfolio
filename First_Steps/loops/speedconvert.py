#this program converts the speed 60kph
#throught 100kph (in 10kph increments)
#to mph

start_speed = 60    #starting speed

end_speed = 131     #ending speed

increments = 10     #speed increments

conversion_factor = .6214

#Print the Table Headings

print('KPH\tMPH')

print('-'*12)

#Print the speeds

for kph in range(start_speed, end_speed, increments):
    mph = kph * conversion_factor

    print(f'{kph}\t{mph:.1f}')