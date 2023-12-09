import _aboutme, _exp, _edu, random, time

def _invalid():    # invalid if user input is not accepted
    print("\n!! invalid option !!\nplease try again...\n")

def _return():    # return to previous menu
    while True:
        opt = str(input("\n'r' to return to previous menu: "))
        if opt == "r":
            break
        else:
            _invalid()
            continue
            
def _divide():    # menu divider
    print("\n\n######################################################################\n")

def menu():    # main menu
    menu_list = ["About me","Experience","Education","Skills","Licenses & Certifications","Interests","Hobbies","exit"]
    while True:
        menu_num = 0
        _divide()
        print("\n>> MAIN MENU:\n")
        for menu_x in menu_list:
            menu_num += 1
            print(str(menu_num) + ". " + menu_x)
        menu_opt = input("\nSelect an option: ")    # user input for main menu selection
        
        if menu_opt == "1":    # main menu 1 - About me
            _divide()
            print("\n>> ABOUT ME:\n")
            print(_aboutme.aboutme)
            _return()               
        elif menu_opt == "2":    # main menu 2 - Experience menu
            while True:
                work_num = 0
                _divide()
                print("\n>> EXPERIENCE menu:\n")    # Eperience menu
                for work_x in _exp.Work.work_list:
                    work_num += 1
                    print(str(work_num) + ". " + work_x)
                work_opt = input("\nSelect an option for more details ('r' to return to main menu): ")  
                if work_opt == "1":    # work option 1 - Excelcom
                    _divide()
                    print(_exp.excelcom.show())
                    _return() 
                elif work_opt == "2":    # work option 2 - s2 Security
                    _divide()
                    print(_exp.s2sec.show())
                    _return()
                elif work_opt == "3":     # work option 3 - Redbook Inspect
                    _divide()
                    print(_exp.rbi.show())
                    _return()
                elif work_opt == "4":    # work option 4 - Subaru Interactive
                    _divide()
                    print(_exp.subie_interactive.show())
                    _return() 
                elif work_opt == "5":    # work option 5 - Subaru Docklands   
                    _divide()
                    print(_exp.subie_docklands.show())
                    _return()
                elif work_opt == "r":    # return to Main menu
                    break
                else:    # invalid option - displays Experience menu
                    _invalid()
                    continue                         
        elif menu_opt == "3":    # main menu option 3 - Education
            _divide()
            print("\n>> EDUCATION:\n")
            _edu.thm.show()
            _edu.ewp_boom.show()
            _edu.yellow_card.show()
            _edu.metro.show()
            _edu.rail.show()
            _edu.inner_range.show()
            _edu.white_card.show()
            _edu.aws_cert.show()
            _edu.solo_py.show()
            _edu.lvt_admin.show()
            _edu.lvt_structural.show()
            _edu.lvt_inspect.show()
            _edu.auto_cert.show()
            _edu.auto_apprentice.show()
            _edu.auto_pre.show()     
            _return()
        elif menu_opt == "4":    # main menu option 4 - Skills
            while True:
                _divide()
                print("\n>> SKILLS:\n")
                for skill_x in _aboutme.skills:
                    print(str("- ") + skill_x)
                _return()
                break
        elif menu_opt == "5":     # main menu option 5 - Licenses & Certifications
            while True:
                _divide()
                print("\n>> LICENSES & CERTIFICATIONS:\n")
                for cert_x in _aboutme.licenses_cert:
                    print(str("- ") + cert_x)
                _return()
                break
        elif menu_opt == "6":    # main menu option 6 - Interest
            while True:
                _divide()
                print("\n>> INTEREST:\n")
                for int_x in _aboutme.interests:
                    print(str("- ") + int_x)
                _return()
                break
            elif menu_opt == "7":    # main menu option 7 - Hobbies
            while True:
                _divide()
                print("\n>> HOBBIES:\n")
                for hob_x in _aboutme.hobbies:
                    print(str("- ") + hob_x)
                _return()
                break
        elif menu_opt == "8":    # main menu option 8 - Exit program
            _divide()
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
