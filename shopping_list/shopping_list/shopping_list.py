

# make a list to hold onto our items
shopping_list = []
print("What should we pick up at the store?")


def show_help():
    # print out instruction on how to use the app    
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' to stop adding items.
Enter 'SHOW' to stop adding items.
""")

def show_list():
    # print out the list
    print("Here's your list:")

    for item in shopping_list:
        print(item)

def add_to_list(new_item):
    # add new items to our list
    shopping_list.append(new_item)
    print ("Added {}. List now has {} items".format(new_item, len(shopping_list)))

def main():

    while True:
        # ask for new items
        new_item = input("> ")

        # be able to quit the app
        if new_item == 'DONE':
            break
        elif new_item == 'HELP':
            show_help()
            continue
        elif new_item == 'SHOW':
            show_list()
            continue
        add_to_list(new_item)
    #show list to user when when loop is exited from
    show_list()
    
#adding a save function    
def open_save():
  print("Enter the name of your file")
  file = input('Enter your name: ')

  try:
       with open(file, 'w') as file:
         for items in shopping_list:
            file.write(str(items) + "\n")
  except:
    print("try again")    

open_save()
show_help()
main()


