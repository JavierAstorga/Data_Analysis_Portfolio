print('\n\n','*'*20, '\n')

# #1. Bug Collector

# bugs_collected = 0

# for bugs in range(1,6):
#     bugs_collected += int(input(f'Enter how many bug you collect in day {bugs}: '))

# print(f'You collect {bugs_collected} in 5 days')



# #2. Calories Burned

# minute = 0

# for cal_burn in range(10,31,5):
#     minute = cal_burn
#     t_cal_burn = 4.2 * minute
#     print(f'You burn {t_cal_burn} calories in {cal_burn} minutes')


# #3. Lap times

# laps = int(input('How many laps you did?: '))

# fast_lap = 0.0
# slow_lap = 0.0
# total_time = 0.0

# for lap in range(laps):
#     lap_time = float(input('Enter Lap Time: '))

#     if lap_time < fast_lap:
#         fast_lap += lap_time
#     if lap_time > slow_lap:
#         slow_lap += lap_time
    
#     total_time += lap_time

# average_time = total_time /laps

# print(f'slow lap: {slow_lap}')
# print(f'Fast lap: {fast_lap}')
# print(f'average: {average_time}')


# #4. Distance traveled

# speed = int(input('Speed vehicle: '))

# hours = int(input('hours traveled: '))

# distance = 0

# print('\nhour\tdistance\n-----------------')
# for i in range(hours+1):
#     distance += speed * hours
#     print(i, '\t', distance, 'mph')


# # 6.Miles to kilometers table
# km = 0.0
# print('miles\t\tkilometers\n','-'*25)
# for i in range(10,81,10):
#     km +=  i * 1.60934
#     print(f'{i}\t\t{km:.2f}')



# # 7.Pennies per day

# days = int(input('Days: '))

# penny = 0.01

# for p in range(1,days+1):
#     print(f'in day {p}, money: ${penny:.2f}')
#     penny = penny * 2



# #9. Ocean Levels

# print('Year\t\tMillimeters\n','-'*25)
# ocean_level = 0.0
# for o in range (1,26):
#     ocean_level += 1.6
#     print(f'{o}\t\t{ocean_level:.2f}ml')


# # 10. Tuition Increase

# tuition = 8000.00
# semester = 1
# for y in range(1,6):
#     tuition += 0.03*tuition
#     print(f'Semester {semester} & {semester+1} in year {y}: {tuition:.2f}')
#     semester += 2


# 11. Sleep debt

input_user = [8,8,8,8,8,8,8]

sleep_hours = 0
for s in range(7):
    sleep_hours += input_user[s]
    print(sleep_hours)
if sleep_hours == 56:
    print('Im jelous')
elif sleep_hours < 56:
    print('you need to sleep more')
elif sleep_hours > 56:
    print('You oversleep')


