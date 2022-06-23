import menu_loop
import random

print("=================\n Huy Tu's Resume\n=================")

auth_count = 3
print("You have 3 chances")

while auth_count <= 3 and auth_count >= 1:
    x_add = random.randrange(0,10)
    y_add = random.randrange(0,10)
    xy_add = x_add + y_add
        
    add = input(f"{x_add} + {y_add} = ")
    auth_count -= 1
    
    if add == xy_add:
        print("Correct!!")
        menu_loop.menu()

    elif add != xy_add and auth_count > 1 and auth_count <= 3:
        print(f"..incorrect\nyou have {auth_count} chances left..")
        continue
    
    elif add != xy_add and auth_count == 1:
        print("..this is your last chance")
        continue
        
    elif auth_count == 0:
        print("\nGandalf: you shall not PASS!!")
        break
    else:
        menu_loop.invalid()
        continue