# string iteration
# using a For loop
# the T goes into ch then printed, than o goes into ch then printed
# etc

name = 'Tommy'

for ch in name:
    print(ch)

print()
print()

# count the T's in the sentence

def main():

    count = 0

    my_string = input('Enter a Sentence: ')

    # count the T's

    for ch in my_string:

        if ch =='T' or ch == 't':
            count = count +1

    print('The letter T appears', count, 'times')

main()

print()
print()


# INDEXING

# Another way to access individual characters in a string is with index

# each char in string has an index that specifies the position on the string

# index starts at 0.

my_string = "Roses are Red"

print(my_string[0], my_string[6], my_string[10])
print()
print()


# 
# Negative Indexes to the end of a string
# -1 identifies the lst char in the string
# -2 second last etc
# d e R

print('Negative Indexes at the end of string')
print(my_string[-1],my_string[-2],my_string[-13])
print()
print()

# IndexError Exceptions
# This will occurif you try to use an index that is out
# of range
# this will cause an error
# city = 'Boston'
# print(city[6])
# The next code will cause an error. The last time this loop iterates
# th inde will be assigned 6, which is an invalid index
# We need to use the len function

city = 'Boston'
index = 0 
while index < 7:
    #print(city[index])
    index = index + 1
print()
print()

city = 'Boston'
index = 0
while index <len(city):     # use the len funciton to make suer you do not have an index error
    print(city[index])
    index = index + 1
print()
print()


# String Slicing
# use slicing expressions to select a range of characters

# aslice is a span of items that are taken from a sequence.
# you get a span of char from within the string
# string slices are called substrings

# get a slice
# string[start: end]

full_name = "Javier Astorga"

middle_name = full_name[0:5]

surname = full_name[-7]


print()



# Assing surname to last_name

print()

last_name = full_name[6:0]

print('My last name is ', last_name)

print()
print()




# Step values start at 0, 26 characters step by 2

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print(letters[0:26:2])

# FINISHED
# Extracting Characters from a string

# the get_lo