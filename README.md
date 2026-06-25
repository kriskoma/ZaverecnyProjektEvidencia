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

Dáta sú uložené v kolekcii v pamäti (nie v databáze). Projekt vznikol ako záverečná práca kurzu Python na ITnetwork Academy, s dôrazom na princípy SRP a SoC.
