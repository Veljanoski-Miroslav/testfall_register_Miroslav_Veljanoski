# Testfallsregistrering

Ett konsolbaserat Python-program för att registrera, validera och visa testfall via en interaktiv terminalmeny.

## Funktioner

* **Registrera testfall:**  Lägg till nya testfall med unikt numeriskt ID, namn och beskrivning.
* **Inmatningsvalidering:**  Säkerställer att ID anges med siffror, att namn och beskrivning inte lämnas tomma samt förhindrar dubbletter av testfalls ID.
* **Visa testfall:** Listar alla registrerade testfall direkt i terminalen.
* **Enhetstester:** Innehåller automatiserade tester skrivna med `pytest`.

## Projektstruktur

```text
├── main.py                         # Programstart och huvudmeny
├── model/
│   └── register.py                 # Datamodell (Register)
├── service/
│   ├── register_menu.py            # Menyhantering och användarinmatning
│   └── register_testcase.py        # Affärslogik och validering
├── utils/
│   └── console_helper.py           # Hjälpfunktioner för konsolen (t.ex. clear_screen)
└── tests/
    └── test_register_testcase.py   # Enhetstester med pytest
```

## Installation & Krav

* **pytest** (för att köra enhetstesterna)

1. Klona eller ladda ner projektet till din dator.
2. Skapa och aktivera en virtuell miljö som till ex. VS Code:

   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   ```
3. Installera `pytest`:
   ```bash
   pip install pytest
   ```

## Användning

Starta programmet från projektets rotmapp:

```bash
python main.py
```

Följ därefter alternativen i menyn för att registrera nya testfall eller lista befintliga.

## Testning av funktioner

För att köra de automatiserade enhetstesterna i terminalen:

```bash
python -m pytest
```
