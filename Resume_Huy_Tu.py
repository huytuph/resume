import menu_loop
import random

print("=================\n Huy Tu's Resume\n=================")

print("enter the correct answer to view my resume\nYou have 3 chances")

auth_count = 3
while auth_count != 0:
    x_add = random.randrange(0,10)
    y_add = random.randrange(0,10)
    xy_add = x_add + y_add
        
    add = input(f"{x_add} + {y_add} = ")
    auth_count -= 1
    
    if add == str(xy_add):
        print("Correct!!")
        menu_loop.menu()

    elif add != xy_add and auth_count > 0 and auth_count <= 3:
        print(f"..incorrect\nyou have {auth_count} chances left..")
        continue
    
    elif auth_count == 0:
        print("\nGandalf: you shall not PASS!!")
        break
    else:
        menu_loop.invalid()
        continue