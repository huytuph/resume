import aboutme_, exp_, edu_, random, time, os


def clear_screen():
    """
    clears screen for all operating systems
    """
    if os.name == 'nt': # 'nt' == windows
        os.system('cls')    # if os = windows:
    else:
        os.system('clear')  # if os = linux/unix:
        
def _invalid():
    """invalid if user input is not accepted"""
    print("\n!! invalid option !!\nplease try again...\n")

def _return():
    """ return to previous menu"""
    while True:
        opt = str(input("\n'r' to return to previous menu: "))
        if opt == "r":
            break
        else:
            _invalid()
            continue

def menu():
    """main menu"""
    menu_list = ["About me","Experience","Education","Skills","Licenses & Certifications","Interests","Hobbies","exit"]
    while True:
        clear_screen()
        menu_num = 0
        print("\n>> MAIN MENU:\n")
        for menu_x in menu_list:
            menu_num += 1
            print(str(menu_num) + ". " + menu_x)
        
        menu_opt = input("\nSelect an option: ")    # user input for main menu selection
        if menu_opt == "1":    # main menu 1 - About me
            clear_screen()
            print("\n>> ABOUT ME:\n")
            print(aboutme_.aboutme)
            _return()
                           
        elif menu_opt == "2":    # main menu 2 - Experience menu
            while True:
                clear_screen()
                work_num = 0
                print("\n>> EXPERIENCE menu:\n")    # Eperience menu
                for work_x in exp_.Work.work_list:
                    work_num += 1
                    print(str(work_num) + ". " + work_x)
                work_opt = input("\nSelect an option for more details ('r' to return to main menu): ")  
                
                if work_opt == "1":    # work option 1 - Excelcom
                    clear_screen()
                    print(exp_.excelcom.show())
                    _return() 
                
                elif work_opt == "2":    # work option 2 - s2 Security
                    clear_screen()
                    print(exp_.s2sec.show())
                    _return()
                
                elif work_opt == "3":     # work option 3 - Redbook Inspect
                    clear_screen()
                    print(exp_.rbi.show())
                    _return()
                
                elif work_opt == "4":    # work option 4 - Subaru Interactive
                    clear_screen()
                    print(exp_.subie_interactive.show())
                    _return() 
                
                elif work_opt == "5":    # work option 5 - Subaru Docklands   
                    clear_screen()
                    print(exp_.subie_docklands.show())
                    _return()
                
                elif work_opt == "r":    # return to Main menu
                    break
                
                else:    # invalid option - displays Experience menu
                    _invalid()
                    continue
                                      
        elif menu_opt == "3":    # main menu option 3 - Education
            clear_screen()
            print("\n>> EDUCATION:\n")
            edu_.thm.show()
            edu_.ewp_boom.show()
            edu_.yellow_card.show()
            edu_.metro.show()
            edu_.rail.show()
            edu_.inner_range.show()
            edu_.white_card.show()
            edu_.aws_cert.show()
            edu_.solo_py.show()
            edu_.lvt_admin.show()
            edu_.lvt_structural.show()
            edu_.lvt_inspect.show()
            edu_.auto_cert.show()
            edu_.auto_apprentice.show()
            edu_.auto_pre.show()     
            _return()
            
        elif menu_opt == "4":    # main menu option 4 - Skills
            while True:
                clear_screen()
                print("\n>> SKILLS:\n")
                for skill_x in aboutme_.skills:
                    print(str("- ") + skill_x)
                _return()
                break
            
        elif menu_opt == "5":     # main menu option 5 - Licenses & Certifications
            while True:
                clear_screen()
                print("\n>> LICENSES & CERTIFICATIONS:\n")
                for cert_x in aboutme_.licenses_cert:
                    print(str("- ") + cert_x)
                _return()
                break
            
        elif menu_opt == "6":    # main menu option 6 - Interest
            while True:
                clear_screen()
                print("\n>> INTEREST:\n")
                for int_x in aboutme_.interests:
                    print(str("- ") + int_x)
                _return()
                break
            
        elif menu_opt == "7":    # main menu option 7 - Hobbies
            while True:
                clear_screen()
                print("\n>> HOBBIES:\n")
                for hob_x in aboutme_.hobbies:
                    print(str("- ") + hob_x)
                _return()
                break
            
        elif menu_opt == "8":    # main menu option 8 - Exit program
            clear_screen()
            print("shutting down in..")
            exit_countdown = 3
            while exit_countdown != 0:
                print(exit_countdown)
                exit_countdown -= 1
                time.sleep(1)
            exit()
            
        else:    # invalid option - displays Main menu
            _invalid()
            continue
