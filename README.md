# Tippmix Pro 5.1 – TippmixPro-központú piaci összehasonlítás

Újdonság: **TippmixPro vs. nemzetközi piac · 1X2**. A rendszer a `data/live.json` külső oddsadatainak legalább két teljes 1X2 piacából árrésmentesített átlagos valószínűséget számol, és ezt a felhasználó által a TippmixPro.hu-n kézzel ellenőrzött oddsszal veti össze.

A mutató **piaci proxy**, nem független valószínűségmodell, nem validált EV és nem fogadási ajánlás. A külső oddsok sosem kerülnek automatikusan TippmixPro-szelvényre. Nincs hivatalos TippmixPro API-kapcsolat.

## Telepítés meglévő 5.0-ra
1. Helyi JSON mentés.
2. Csak `index.html`, `sw.js`, `README.md` cseréje a GitHub repository gyökerében.
3. A `.github`, `scripts`, `data` mappák megőrzése.
4. GitHub Pages telepítés után az Elemzés menüben keresd a TippmixPro vs. nemzetközi piac panelt.

A helyi tárolási kulcs változatlan: `tippmixpro-v1`. A statisztikai adatokat továbbra is külön forrásból kell majd integrálni.
