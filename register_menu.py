import time
from utils.console_helper import clear_screen
from service.register_testcase import RegisterTestcase


class RegisterMenu:
    def __init__(self):
        self.register = RegisterTestcase()

    def display_register(self):
        while True:
            clear_screen()
            print("### Välkommen till testfall registrering ###")
            print("Vänligen välj ett alternativ nedan:\n")
            print("1. Registrera nytt testfall")
            print("2. Visa alla registrerade testfall")
            print("3. Tillbaka till huvudmenyn\n")

            choice = input("Ange ditt val (1-3): ").strip()

            match choice:
                case "1":
                    self._add_testcase()
                case "2":
                    clear_screen()
                    self.register.display_registers()
                    input("\nTryck Enter för att fortsätta...")
                case "3":
                    break
                case _:
                    print("Ogiltigt val. Vänligen försök igen.\n")
                    time.sleep(2)

    def _add_testcase(self):
        clear_screen()
        try:
            testcase_id = int(input("Testfall ID: ").strip())
        except ValueError:
            print("Testfall ID måste anges med siffror.")
            time.sleep(2)
            return

        name = input("Testfall Namn: ").strip()
        description = input("Testfall Beskrivning: ").strip()

        try:
            self.register.add_register(testcase_id, name, description)
        except ValueError as e:
            print(f"\n{e}")
            time.sleep(2)
            return

        print("\nTestfallet har registrerats:")
        print(f"ID: {testcase_id}, Namn: {name}, Beskrivning: {description}")
        time.sleep(2)
