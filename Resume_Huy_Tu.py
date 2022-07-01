import menu_loop, random, time

# 3 second countdown timer before the program starts
print("starting in..")
start_countdown = 3
while start_countdown != 0:
    print(start_countdown)
    start_countdown -= 1
    time.sleep(1)

print("=================\n Huy Tu's Resume\n=================")

# a simple math problem challenge for the users to enter the main menu
# will randomly generate a new math problem if answered incorrectly
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
    
    # Gandalf will deny you access to my resume if you have answered incorrectly 3 times
    elif auth_count == 0:
        print("\nGandalf: you shall not pass4!!")
        break
    else:
        menu_loop.invalid()
        continue