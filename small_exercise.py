# Instrutions:


# The starter code provides you with the main menu for a command-line
# based grocery list application.

# The user should be able to add, update, and remove items.
# Small exercise ------------------------------------------------
# Using this starter code, you're going to combine the pieces of code
# you've written so far to create the functionality for each action (either 
# adding, updating, or removing an item).

# Each time the user adds, updates, or deletes an item, they should see the main menu again.

# Start with an empty grocery list
groceries = []

main_menu = '''

1. Print List
2. Add Items
3. Edit Items
4. Remove Items
5. Quit

'''

while True:
    menu_choice = int(input(main_menu))

    # Add if/else statements for each menu item
    if menu_choice == 1:
        # Print the grocery list with indexes
        indexes = range(len(groceries))
        for i in indexes:
            item = groceries[i]
            print(f'{i}: {item}')

    # Add items
    elif menu_choice == 2:
        while True:
            item = input('What do you need from the store? ')

            if item == '':  # Alternatively: check if len(item) == 0
                break
            groceries.append(item)
        print(main_menu)
    
    # Edit items
    elif menu_choice == 3:
        # Give them the chance to replace 
        start_index_to_replace = int(input('What start index to replace? '))
        end_index_to_replace = int(input('What end index to replace? '))

        if start_index_to_replace == end_index_to_replace:
            # Prompt the user for the new item
            new_item = input('What is the new item? ')

            # - replace the item at that index with the new item
            groceries[start_index_to_replace] = new_item

        else:
            # gather replacements
            replacements = []
            while True:
                new_item = input('What is the new item? ')
                if new_item == '':
                    break
                replacements.append(new_item)
            groceries[start_index_to_replace:end_index_to_replace] = replacements
            
    # Remove items
    elif menu_choice == 4:
        # Give them the chance to remove
        start_index_to_remove = int(input('What start index to remove? '))
        end_index_to_remove = int(input('What end index to remove? '))

        if start_index_to_remove == end_index_to_remove:
            # Delete the item at start_index_to_remove from list
            del groceries[start_index_to_remove]
        
        else:
            # Delete items in range from list
            del groceries[start_index_to_remove:end_index_to_remove + 1]
            
    # Exit app
    elif menu_choice == 5:
        break

print('Thank you for using the grocery list app!')
