from itertools import count
import menu_loop
import random
import time

print("starting in..")
countdown = 3
while countdown != 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)

print("=================\n Huy Tu's Resume\n=================")

print("enter the correct answer to view my resume\nYou have 3 chances")


auth_count = 3
while auth_count != 0:
    x_add = random.randrange(0,10)
    y_add = random.randrange(0,10)
    xy_add = x_add + y_add
        
    add = input(f"\n{x_add} + {y_add} = ")
    auth_count -= 1
    
    if add == str(xy_add):
        print("Correct!!")
        menu_loop.menu()

    elif add != xy_add and auth_count > 0 and auth_count <= 3:
        print(f"..incorrect\nyou have {auth_count} chances left..")
        continue
    
    elif auth_count == 0:
        print("\nGandalf: you shall not pass4!!")
        break
    else:
        menu_loop.invalid()
        continue