# Insurance Registry

Konzolová aplikácia v Pythone na správu poistených osôb.

## Funkcie

- Vytvorenie poisteného (meno, priezvisko, vek, telefónne číslo)
- Zobrazenie zoznamu všetkých poistených
- Vyhľadanie poisteného podľa mena a priezviska

## Spustenie

```bash
python main.py
```

## Štruktúra projektu

- `main.py` – ovládanie aplikácie a komunikácia s užívateľom
- `insured_person.py` – entita poisteného (validácia vstupov, konštruktor)
- `insurance_manager.py` – správa kolekcie poistených (uloženie, vyhľadávanie)
- `tests/test_insured_person.py` – testy validácie vstupov a výstupu entity poisteného
- `tests/test_insurance_manager.py` – testy pridávania, zobrazenia a vyhľadávania poistených
- `pytest.ini` – konfigurácia pytestu

Dáta sú uložené v kolekcii v pamäti (nie v databáze). Projekt vznikol ako záverečná práca kurzu Python na ITnetwork Academy, s dôrazom na princípy SRP a SoC.

## Testy

Projekt obsahuje automatické testy napísané v [pytest](https://docs.pytest.org/). Pokrývajú:

* validáciu vstupov (prázdne mená, neplatný vek, neplatné telefónne číslo vrátane hraničných hodnôt),
* pridávanie a zobrazenie poistených,
* vyhľadávanie podľa mena a priezviska (bez ohľadu na veľkosť písmen, nenájdený záznam, viac osôb s rovnakým menom).

Spustenie testov:

```
pip install pytest
pytest
```