# this program demostrates how to get 

def main():
    #create a list

    food = ['Burger', 'Pizza', 'Chips']

    # display the list

    print(' Here are the items in the food list')

    print(food)

    # get the item yu want to change


    item = input('Which item should i change: ')

    try:
        # get the item's index in the list. In our case we want to replace pizza
        # with potatoses looking for the index which in this case is 0 because pizza
        # food.index(item) pizza is the item. looking fiur the index in thar index
        # is 0 because we are replacing pizza

        item_index = food.index(item)

        # get the value to replace it with

        new_item = input('Enter the new Item: ')

        # replace the old item with the New Item

        food[item_index] = new_item

        # display the list

        print('Here is the revised list')

        print(food)

    except ValueError:
        print('That itme was not found in the list')

main()
