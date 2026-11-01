# Tippmix Pro 6.0 – Online Intelligence

Újratervezett mobil PWA. V3 CSV-import és kézi eseményűrlap eltávolítva a felületről. Automatikus online oddsbetöltés a meglévő `data/live.json` fájlból; sportág szerinti keresés; teljes 1X2 / kétkimenetelű győztes piacok árrésmentesített konszenzusa; legjobb külső odds és iroda megnevezése; figyelőlista; régi virtuális szelvények csak olvasható megjelenítése; JSON-mentés. Az eredeti `tippmixpro-v1` localStorage adat nem változik.

**Fontos:** az „Adatfájl újraellenőrzése” gomb csak a GitHub Pages fájlt olvassa újra. Nem futtat GitHub Actions munkafolyamatot és nem kér közvetlenül odds API-t. A forrásfrissítés időbélyege és a telefonos lekérés időpontja külön látható. A meglevő `scripts`, `data` és `.github` mappákat hagyd érintetlenül. A `data/live.json` csomagban nem szerepel: a már működő távoli adatfolyamot nem írjuk felül üres mintával.

**Telepítés:** előbb JSON-mentés a régi alkalmazásban, majd a repo gyökerében kizárólag `index.html`, `sw.js`, `README.md` cseréje. Az ikonokat és manifestet nem szükséges frissíteni. Commit `main` ágra, várj GitHub Pages közzétételre, nyisd meg Safari alatt, szükség esetén frissítsd az oldalt.

**Határok:** a jelenlegi The Odds API integráció a korlátozott kvótájú, kiválasztott ligákra vonatkozó feedet adja; nem garantálja az összes irodát vagy minden sporteseményt. A számított fair odds nem önálló sportstatisztikai modell. TippmixPro.hu oddsadatokhoz nincs hiteles automatikus kapcsolat. A figyelőlista nem fogadási szelvény, a rendszer nem köt fogadást.
