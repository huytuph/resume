import _menu, random, time

myname = [
"--------------------------------------------------------------",
"  _   _         _   _   _____          ____  _                ",
" | |_| | _   _ | |_| | |_   _| _   _  |  . || |_  ___  _____  ",
" |  _  || |_| ||___  |   | |  | |_| | | ___||   |/.  ||     | ",
" |_| |_||_____||_____|   |_|  |_____| |_|   |_|_||_|_||_|_|_| ",
"--------------------------------------------------------------",
" "
]
for x in myname:
    print(x)
    time.sleep(0.1)

# a simple math challenge for the users to enter the main menu
# will randomly generate a new math problem if answered incorrectly
time.sleep(1)
print("enter the correct answer to view my resume\nYou have 3 chances")
auth_count = 3
while auth_count != 0:
    x_add = random.randrange(0,12)
    y_add = random.randrange(0,12)
    xy_add = x_add + y_add    
    add = input(f"\n{x_add} + {y_add} = ")
    auth_count -= 1
    if add == str(xy_add):    # correct answer - displays Main menu
        print("Correct!!")
        _menu.menu()
    elif add != xy_add and auth_count > 0 and auth_count <= 3:    # generates math challenge
        print(f"..incorrect\nyou have {auth_count} attempts left..")
        continue
    elif auth_count == 0:    # Gandalf will deny you access to my resume if you have answered incorrectly 3 times
        print("\nGandalf: you shall not pass!!")
        break
    else:
        _menu.invalid()
        continue    # invalid option - displays math challenge
