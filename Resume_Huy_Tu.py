
import resume_var
import exp_class
import edu_class
import random

def invalid():
    print("\n!! invalid option !!\nplease try again...")

print("=================\n Huy Tu's Resume\n=================")

menu_list = ["About me","Experience","Education","Hobbies","Interests","Ctrl+C to quit"]

auth_count = 3
print("You have 3 chances")

while auth_count <= 3 and auth_count >= 1:
    x_add = random.randrange(0,10)
    y_add = random.randrange(0,10)
    xy_add = x_add + y_add
        
    add = int(input(f"{x_add} + {y_add} = "))
    auth_count -= 1
    
    if add == xy_add:
        print("Correct!!")
        while True:
            menu_num = 0
            print(">> Main Menu:")
            for menu_x in menu_list:
                menu_num += 1
                print(str(menu_num) + ". " + menu_x)
        
            menu_opt = input("\nSelect an option: ")
            if menu_opt == "1":
                print("\n>> About Me:")
                print(resume_var.aboutme)
                while True:
                    aboutme_opt = str(input("'r' to return to main menu: "))
                    if aboutme_opt == "r":
                        break
                    else:
                        invalid()
                        False
                
            elif menu_opt == "2":
                while True:
                    work_num = 0
                    print("\n>> Experience")
                    for work_x in exp_class.Work.work_list:
                        work_num += 1
                        print(str(work_num) + ". " + work_x)
                    work_opt = input("\nSelect an option for more details ('r' to return to main menu): ")
            
                    if work_opt == "1":
                        print(exp_class.s2sec.show())
                        while True:
                            s2sec_opt = str(input("'r' to return to Experience menu: "))
                            if s2sec_opt == "r":
                                break
                            else:
                                invalid()
                                continue
                    
                    elif work_opt == "2":
                        print(exp_class.rbi.show())
                        while True:
                            rbi_opt = str(input("'r' to return to Experience menu: "))
                            if rbi_opt == "r":
                                break
                            else:
                                invalid()
                                continue
                    
                    elif work_opt == "3":
                        print(exp_class.subie_werribee.show())
                        while True:
                            subw_opt = str(input("'r' to return to Experience menu: "))
                            if subw_opt == "r":
                                break
                            else:
                                invalid()
                                continue
                    
                    elif work_opt == "4":
                        print(exp_class.subie_interactive.show())
                        while True:
                            subi_opt = str(input("'r' to return to Experience menu: "))
                            if subi_opt == "r":
                                break
                            else:
                                invalid()
                                continue
                    
                    elif work_opt == "5":
                        print(exp_class.subie_docklands.show())
                        while True:
                            subd_opt = str(input("'r' to return to Experience menu: "))
                            if subd_opt == "r":
                                break
                            else:
                                invalid()
                                continue
                    elif work_opt == "r":
                        break
                    else:
                        invalid()
                        continue
                  
            elif menu_opt == "3":
                print("\n>> Education:")
                edu_class.lvt_admin.show()
                edu_class.lvt_structural.show()
                edu_class.lvt_inspect.show()
                edu_class.auto_cert.show()
                edu_class.auto_apprentice.show()
                edu_class.auto_pre.show()     
                while True:    
                    edu_opt = str(input("'r' to return to main menu: "))
                    if edu_opt == "r":
                        break
                    else:
                        invalid()
                        continue

            elif menu_opt == "4":
                while True:
                    print("\n>> Hobbies:\n")
                    for hob_x in resume_var.hobbies:
                        print(str("- ") + hob_x)
                    while True:
                        hob_opt = str(input("\n'r' to return to main menu: "))
                        if hob_opt == "r":
                            break
                        else:
                            invalid()
                            continue
                    break

            elif menu_opt == "5":
                while True:
                    print("\n>> Interests:\n")
                    for int_x in resume_var.interests:
                        print(str("- ") + int_x)
                    while True:
                        int_opt = str(input("\n'r' to return to main menu: "))
                        if int_opt == "r":
                            break
                        else:
                            invalid()
                            continue
                    break
    
            else:
                invalid()
                continue

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
        invalid()
        continue