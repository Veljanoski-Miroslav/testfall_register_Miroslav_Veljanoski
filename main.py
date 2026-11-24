
from utils.console_helper import clear_screen
import time
from service.register_menu import RegisterMenu



def main():
    
    
    while True:
        clear_screen()
        
        print("### Välkommen till testfallsregistrerings programmet ###\n")
        print("Välj ett av följande alternativ")
        print("1. Registrera testfall")
        print("2. Avsluta programmet")

        user_choice = input()
        match user_choice:
            case "1": 
                RegisterMenu().display_register()
            case "2": 
                clear_screen()
                print ("Tack för besöket! \n Programmet avslutas")
                time.sleep(2)
                quit()
            case _:
                clear_screen()
                print("Ogiltigt val, vänligen försök igen")
                time.sleep(2)
                main()

if __name__ == "__main__":
    main()
    


    



