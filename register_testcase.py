from model.register import Register
from utils.console_helper import clear_screen
import time

class RegisterTestcase:
    def __init__(self):
        self.registers: list[Register] = []

    def add_register(self, testfall_id: int, testfall_name: str,
                     testfall_description: str) -> Register:
        if not testfall_name:
            raise ValueError("Testfall Namn kan inte vara tomt.")
        if not testfall_description:
            raise ValueError("Testfall Beskrivning kan inte vara tomt.")
        if any(r.testfall_id == testfall_id for r in self.registers):
            clear_screen()
            raise ValueError(f"Testfall ID {testfall_id} finns redan.Vänligen ange annat ID för att kunna registrera testfallet!\n")
            time_wait(5)
            self.add_register()


        register = Register(testfall_id, testfall_name, testfall_description)
        self.registers.append(register)
        return register

    def display_registers(self):
        if not self.registers:
            print("Inga testfall har registrerats än.")
            return

        print("\n### Registrerade Testfall ###")
        for r in self.registers:
            print(f"ID: {r.testfall_id}")
            print(f"Namn: {r.testfall_name}")
            print(f"Beskrivning: {r.testfall_description}\n")
