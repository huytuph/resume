
import resume_var, exp_class, edu_class, random, time

# invalid function prints if user input is not accepted
def invalid():
    print("\n!! invalid option !!\nplease try again...\n")

def divide():
    print("\n\n#######################################################################################\n")

# menu function loop
def menu():
    
    # menu list
    menu_list = ["About me","Experience","Education","Skills","Licenses & Certifications","Interests","Hobbies","exit"]
    
    # main menu
    # prints all Main menu options from menu_list
    while True:
        menu_num = 0
        divide()
        print("\n>> MAIN MENU:\n")
        for menu_x in menu_list:
            menu_num += 1
            print(str(menu_num) + ". " + menu_x)

        # User input for main menu selection
        menu_opt = input("\nSelect an option: ")
        
        # Main menu 1 - prints About me information imported from resume_var.py
        if menu_opt == "1":
            divide()
            print("\n>> ABOUT ME:\n")
            print(resume_var.aboutme)
            
            # User input for option to return to main menu
            while True:
                aboutme_opt = str(input("'r' to return to main menu: "))
                if aboutme_opt == "r":
                    break
                else:
                    invalid()
                    False
        
        # Main menu 2 - Experience submenu                          
        elif menu_opt == "2":
            
            # Prints all previous places of work from exp_class.py
            while True:
                work_num = 0
                divide()
                print("\n>> EXPERIENCE menu:\n")
                for work_x in exp_class.Work.work_list:
                    work_num += 1
                    print(str(work_num) + ". " + work_x)
                
                # user input for submenu options
                work_opt = input("\nSelect an option for more details ('r' to return to main menu): ")
            
                # work option 1 - prints details about work at Excelcom
                if work_opt == "1":
                    divide()
                    print(exp_class.excelcom.show())
                    while True:
                        excelcom_opt = str(input("'r' to return to Experience menu: "))
                        if excelcom_opt == "r":
                            break
                        else:
                            invalid()
                            continue
                
                # work option 2 - prints details about work at s2 Security
                elif work_opt == "2":
                    divide()
                    print(exp_class.s2sec.show())
                    while True:
                        s2sec_opt = str(input("'r' to return to Experience menu: "))
                        if s2sec_opt == "r":
                            break
                        else:
                            invalid()
                            continue

                # work option 3 - prints details about work at Redbook Inspect
                elif work_opt == "3":
                    divide()
                    print(exp_class.rbi.show())
                    while True:
                        rbi_opt = str(input("'r' to return to Experience menu: "))
                        if rbi_opt == "r":
                            break
                        else:
                            invalid()
                            continue
                
                # work option 4 - prints details about work at Subaru Interactive
                elif work_opt == "4":
                    divide()
                    print(exp_class.subie_interactive.show())
                    while True:
                        subint_opt = str(input("'r' to return to Experience menu: "))
                        if subint_opt == "r":
                            break
                        else:
                            invalid()
                            continue
                
                # work option 5 - prints details about work at Subaru Docklands    
                elif work_opt == "5":
                    divide()
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
        
        # Main menu option 3 - Prints Education details from edu_class.py                         
        elif menu_opt == "3":
            divide()
            print("\n>> EDUCATION:\n")
            edu_class.thm.show()
            edu_class.ewp_boom.show()
            edu_class.yellow_card.show()
            edu_class.metro.show()
            edu_class.rail.show()
            edu_class.inner_range.show()
            edu_class.white_card.show()
            edu_class.aws_cert.show()
            edu_class.solo_py.show()
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

        # Main menu option 4 - prints Skills from resume_var.py
        elif menu_opt == "4":
            while True:
                divide()
                print("\n>> SKILLS:\n")
                for skill_x in resume_var.skills:
                    print(str("- ") + skill_x)
                while True:
                    skill_opt = str(input("\n'r' to return to main menu: "))
                    if skill_opt == "r":                            
                        break
                    else:
                        invalid()
                        continue
                break
        
        # Main menu option 5 - prints Licenses & Certifications from resume_var.py
        elif menu_opt == "5":
            while True:
                divide()
                print("\n>> LICENSES & CERTIFICATIONS:\n")
                for cert_x in resume_var.licenses_cert:
                    print(str("- ") + cert_x)
                while True:
                    cert_opt = str(input("\n'r' to return to main menu: "))
                    if cert_opt == "r":
                        break
                    else:
                        invalid()
                        continue
                break
            
       # Main menu option 6 - prints Interest from resume_var.py
        elif menu_opt == "6":
            while True:
                divide()
                print("\n>> INTEREST:\n")
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
       
       # Main menu option 7 - prints Hobbies from resume_var.py
        elif menu_opt == "7":
            while True:
                divide()
                print("\n>> HOBBIES:\n")
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


       # Main menu option 8 - exit program
       # 3 second countdown timer on exit
        elif menu_opt == "8":
            divide()
            print("shutting down in..")
            exit_countdown = 3
            while exit_countdown != 0:
                print(exit_countdown)
                exit_countdown -= 1
                time.sleep(1)
            exit()
    
        else:
            invalid()
            continue
