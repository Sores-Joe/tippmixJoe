# Tippmix Pro 2.0

Offline-first, magyar nyelvű sportelemző PWA. Nem hivatalos Tippmix-termék, nincs élő odds vagy automatikus sportadat.

## GitHub Pages
Töltsd fel a fájlokat a repository gyökerébe, majd Settings > Pages > Deploy from a branch > main > / (root). A `index.html`, `sw.js`, `manifest.webmanifest` és az ikonok maradjanak együtt.

## Frissítés az 1.0-ról
A v2 megtartja a `tippmixpro-v1` helyi tárhely-kulcsot, így azonos domainen és böngészőben megmaradnak az adatok. Frissítés előtt a Napló menüben készíts JSON mentést. GitHub Pages frissítés után a PWA cache legfeljebb néhány újratöltés után frissül.

## Új funkciók
- Sportág- és szövegszűrés
- Forrás, időbélyeg, eseménykezdés, modell megalapozottságának rögzítése
- Elavult odds és hiányos elemzés figyelmeztetés
- Dokumentációs minőség kijelzése
- Lezárt szelvények realizált ROI-ja
- Szigorúbb JSON importellenőrzés
- Frissülő offline cache

## Korlátok
A pozitív EV csak kézi becslésen alapul, a minőségi jelzés nem igazolja a valószínűségbecslést. A kombinált szelvények függetlenség-feltételezése téves lehet. A napló nem szinkronizál eszközök között.
