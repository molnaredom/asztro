# Asztroprogram 2.1.0

## Mi az asztrológia?
- Szimbolikus következtetőrendszer, amiben idő minőségét vizsgáljuk. Tulajdonképpen egy időpillanat elemzéséről van szó, amire különböző szimbólumoket helyezve, különböző következtetésekre juthatunk.
- Nem összetévesztendő a "vásári" asztrológia ,amit az újságban olvashatunk összefüggéstelen "jóslatokkal" és a valódi asztrológia, ami teljesen racionális alapokon fekszik és matematikai számításokat használ fel.
- Az asztrológiában különböző csoportokat, halmazokat tudunk megkülönböztetni(Csillagjegyek(12), Házak(12), Bolygók(10), Fényszögek(~6)) és ezeknek vehetjük kombinációit is, amik megfigyelsések alapján különböző életterületek megoldására utalnak, mutatnak.
- A következő képlet, az égbolt vázlatos rajza egy adott pillanatban, ebből tudunk adatokat kinyerni.

<p align="center">
  <img src="https://user-images.githubusercontent.com/77636185/138847759-e8614944-8984-4bd0-b738-eafbf976cd1e.png"/>
</p>

## Cél:
- A projektemben szeretnék az informatika, a matematika és az asztrológia vegyítésével egy olyan programot létrehozni, ami különböző módokon segíti előre a használó életvezetési tanácsadás szempontjából.
- Egy Python Django backendel megvalósított webes felületen legyenek elérhetőek a később tárgyalt adatok, funkciók.
- Asztrológia validálása: Vajon valóban pontos elemzést tud adni az asztrológia minden emberre? Milyen pontossággal tud szakterületet javasolni egy ismeretlen embernek, is ismert amberek alapján?


## Megvalósítandó mérföldkövek, funkciók
- [x] horoszkóp szerkezetének implementálása, adatbázisban kezelhetővé tétele
  -  A további adatok feldolgozásához, szükség van egy struktúrára, amiben könnyen kezelhetőek az adatok
- [ ] Adatbázis feltöltése ~ 7 hét
  - Emberek adatainak beszerzése, strukturált tárolása (~ 400-1000 ember)
  - Analógiák feltöltése: Bolygók, Jegyek, Házak és kombinációik (562 oldal)
- [ ] Pályaválasztás segítő program ~ 15 hét
  - Neuronhálók segítségével valószínűségi értékek szabása a különböző munkaterületekre a felhasználónak
  - Ez az asztrológia validálására is lehetőséget biztosít 
- [ ] Analógia gyakorló ~ 2 hét
  - Játékos módon lehessen az egymással analóg személyiségjellemzőket, tárgyakat, színeket, stb. dolgokat pároztatni.
- [ ] Általános elemzés ~ 6 hét
  - Sorstípus: független/kiszolgáltatott/önfeláldozó/áldozat
  - Felosztások: Évszak- Minőség- Elemek- szerinti felosztás
  - Rejtett aszcendens
  - Célkijelölő vagy Megvalósító
  - "Asztro cikk-cakk"
  - Hyleg/Anaréta meghatározása
  - Sérült minta Nap/Hold
 
- [ ] Születési idő pontosítás ~ 15 hét (ha gyorsabban haladnék a vártnál)
  - Ha egy embernek nem tudjuk pontosan mikor született, de történtek már kardinális események az életében. Vissza lehet számolni, pontosan hány óra hány perckor született.

      
### Pályaválasztási kiértékelésről részletesen
- Neuronháló felpéítése
  - Input rétegben megkapja a különböző szempontok analógiáit(6 os ház jegye, hold jegye, 6 os ház ura, 5. ös ház, 3 mas ház, 9 es ház...stb).
  Ezzeket a születési képletből lehet kiolvasni
  - Output rétegen a különböző munkákra fog predikciót adni a gépünk egy-egy valószínűségi százalék formájában(pl 0.26- cégvezetői munka, 0.80 hogy irodai alkalmazott...stb)

### Program indítása
```
pip3 install requirements.txt
cd .\weboldal\
python3 .\manage.py makemigrations base
python3 .\manage.py migrate
python3 .\manage.py runserver
```


### Érdeklődni: 
- Molnár Ádám 
- molnaradam8466@gmail.com 

## Pár szó magamról: 
- 3.féléves programtervező informatikus szakra járok.
- Szegeden a TTIK-n a Szoftverfejlesztő tanszéken dolgozok. Itt adatok kinyerésével és feldolgozásával foglalkozunk.
- Régebb óta érdekelnek spirituális, pszichológiai dolgok, köztük gyereknevelés, oktatás, absztrakt/elvont gondolkodásmódok, lelki segítségnyújtás, tanulási technikák, tudatalatti, tudatosság. És még ezen kívül sok más. 

### A terv fejlődési pontjai:
- 1.0.0 2021 marc.30
- 1.1.0 2021 maj.31
- 1.1.1 2021. jun 2.
- 1.1.2 2021 jun 6.
- 2.0.0 2021 okt. 26.
- 2.0.1 2021 okt.28.
- 2.1.0 2022 jan.8.



#### Hosszútávú tervek:
- Szövegfeldolgozással kinyerni az analógiáknak az értelmét mesterséges intelligenciával, ezáltal kérdéseket feltenni élethelyzet pontosításhoz.
- Számítógép grafikával létrehozni 3d- képlet modelleket a könyebb értelmezhetőség érdekében

#### *korábbi ötletek(NEM RELEVÁNS MÁR)*
- A személyiségmodellben egyes analógia csoportkörök pont értéket fognak kapni. A megkapott értékek alapján egy optimális küszöbindexet határozunk meg.
Amelyik tulajdonság átlépi a küszöbindexet, belekerül az eredményhalmazba.

- A tulajdonságok közt súlyozott gráfokkal döntjük el a szinonima, ellentettszavak kapcsolatát.(ezek előre definináltak, az alaphalmaz elemei)

