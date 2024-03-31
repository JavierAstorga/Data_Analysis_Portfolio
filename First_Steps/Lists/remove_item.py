# this program demonstrates how to use the remove method to remove an item 
# from a list

def main():

    # create a list with some items

    food = ['Pizza', 'Burgers', 'Chips']

    # display the list

    print('Here are the main items in the food list')

    print(food)

    # get the item to remove

    item = input('Which item should I remove')

    try: 
        # remove the item

        food.remove(item)

        # display the list

        print('Here is the Revised list')

        print(food)

    except ValueError:

        print('The item was not found in the list')

main()