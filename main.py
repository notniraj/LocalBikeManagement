import operations as opt

def main():
    continueLoop = True
    opt.welcome_message();
    opt.display_main_menu();
    while continueLoop == True:
        continuationCode = input("Enter the menu code: ")
        if continuationCode == "1":            
            opt.sellBike()
        elif continuationCode == "2":
            opt.orderBike()
        elif continuationCode == "3":
            opt.exit()
            opt.update_file()
            continueLoop = False
        else:
            opt.display_invalid_menu_input()
main()