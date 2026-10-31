# Tippmix Pro 4.1 – külső oddsok, ingyenes kvótával

## Mit csinál?
A GitHub Actions naponta egyszer lekéri a The Odds API ingyenes csomagjából a kiválasztott aktív sportágak legfeljebb 5 ligájának 1X2/győztes (`h2h`) piacait az EU régióban. A feed kizárólag az API által adott valódi bookmaker oddsokat tartalmazza, nem Tippmix oddsokat. A kiválasztás a foci EPL/Bundesliga/Serie A, valamint egy-egy elérhető tenisz/darts kulcs. Az aktív sportágak kínálata változhat, és egyes sportágak hiányozhatnak.

**Nincs automatikus valószínűségbecslés vagy +EV-tipp.** A webalkalmazásban az online eseményt átveheted az Elemzés menübe, ahol a becsült esélyt és indoklást továbbra is külön kell ellenőrizni. A feed 2 óra után elavult jelzést mutathat, mivel az ingyenes kvóta védelmében naponta frissítünk. Ez nem valós idejű odds-szolgáltatás.

## Telepítés
1. A korábbi verzióból készíts JSON biztonsági mentést.
2. Töltsd fel a ZIP tartalmát a `Sores-Joe/tippmixJoe` repo `main` ágának gyökerébe, a `.github/workflows/refresh.yml` és `scripts/fetch_feed.py` almappákat is.
3. Regisztrálj a **https://the-odds-api.com/** címen (ne keverd össze a theoddsapi.com-mal), és kérj API-kulcsot.
4. GitHub repo → Settings → Secrets and variables → Actions → New repository secret: **Name** `ODDS_API_KEY`, **Secret** a kapott kulcs. Soha ne tedd a kulcsot `index.html`-be vagy nyilvános fájlba.
5. GitHub repo → Settings → Actions → General → Workflow permissions → Read and write permissions (ha szükséges; egyes fiókoknál adminisztratív korlátozás lehet).
6. Actions → **Tippmix Pro – ellenőrzött oddsok** → Run workflow. Várd meg a zöld pipát, majd ellenőrizd a `data/live.json` tartalmát és az alkalmazás Online menüjét.
7. A Pages marad `main` és `/ (root)`. A PWA gyorsítótár miatt szükség lehet újratöltésre.

## Költség- és adatminőség-védelem
- Legfeljebb 5 liga × 1 régió × 1 piac = legfeljebb kb. 5 kredit/futás; napi egy futás ~150 kredit/30 nap, ha minden liga aktív. Az API által jelentett fogyasztás a mérvadó.
- A `/sports` lekérdezés ingyenes a dokumentáció szerint.
- Csak 12 órán belül frissített, jövőbeli, 10 napon belüli események kerülnek be.
- A sportágak tényleges lefedettsége, szolgáltatói licenc és API-szerződés feltételei ellenőrzendők.
- Az `index.html` csak publikus `data/live.json`-t olvas; a kulcs soha nem kerül a böngészőbe.
- A `data/live.json` nyilvánosan látható; ne tárolj benne személyes vagy titkos adatot.
- A darts és tenisz történeti statisztikái későbbi külön integrációk, nem részei ennek a csomagnak.
