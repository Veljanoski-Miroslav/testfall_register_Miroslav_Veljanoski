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
## Designreflektion

Programmet är uppdelat i fyra filer, och det syns i diagrammen. `main.py` startar programmet och visar huvudmenyn. När användaren väljer att registrera ett testfall skapas `RegisterMenu`, som sköter hela dialogen med användaren. Menyn känner en `RegisterTestcase`, och det är den som håller ordning på testfallen. När ett testfall är ifyllt skapas ett `Register`, som bara beskriver ett enskilt testfall. Både `main.py` och `RegisterMenu` använder `console_helper` när skärmen ska rensas eller när programmet väntar på att användaren trycker Enter.

Aktivitetsdiagrammet visar samma sak som koden gör, steg för steg: programmet visar menyn, läser av vad användaren valde och gör olika saker beroende på valet. Sekvensdiagrammet visar ett enda varv, alltså vad som händer när användaren registrerar ett testfall hela vägen från meny till sparat testfall.

Uppdelningen gör koden lätt att läsa. Varje fil har sin uppgift, och namnen i koden är samma som i diagrammen. Det går därför att titta på en bild och sedan hitta raden i koden utan att leta. Den gör också koden lätt att ändra.

Testningen blir enklast för den del som bara hanterar data. `RegisterTestcase` tar emot id, namn och beskrivning och sparar dem, och det går att testa direkt utan att skriva något på tangentbordet. Själva menyerna är svårare att testa, eftersom de läser från tangentbordet och skriver på skärmen. Det är ändå en fördel att reglerna för vad som är ett giltigt testfall ligger i `RegisterTestcase` och inte i menyn.


