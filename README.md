# Asztroprogram 2.5.1 Szakdolgozat 1. félév

## Mi az asztrológia?
- Szimbolikus következtetőrendszer, amiben idő minőségét vizsgáljuk. Tulajdonképpen egy időpillanat elemzéséről van szó, amire különböző szimbólumokat helyezve, különböző következtetésekre juthatunk.
- Nem összetévesztendő a "vásári" asztrológia ,amit az újságban olvashatunk összefüggéstelen "jóslatokkal" és a valódi asztrológia, ami teljesen racionális alapokon fekszik és matematikai számításokat használ fel.
- Az asztrológiában különböző csoportokat, halmazokat tudunk megkülönböztetni(Csillagjegyek(12), Házak(12), Bolygók(10), Fényszögek(~6)) és ezeknek vehetjük kombinációit is, amik megfigyelsések alapján különböző életterületek megoldására utalnak, mutatnak.
- A következő képlet, az égbolt vázlatos rajza egy adott pillanatban, ebből tudunk adatokat kinyerni.

<p align="center">
  <img src="https://user-images.githubusercontent.com/77636185/138847759-e8614944-8984-4bd0-b738-eafbf976cd1e.png"/>
</p>

## Cél:
- Webes felületen elérhető alkalmazás, ahol a funkciók elérhetőek.
- End to end Hivatás prediktálás az asztrológia eszközével

## Hivatás prediktálás

> A hivatás predikció 2 modell összevetésével történik
- Mindkét módszernél a felhasználónak meg kell adni születési adatait
- Majd ki kell töltenie egy kérdőívet, ami segít a horoszkóp bepotosításában.
- A kész horoszkópon lehetőségünk van különböző asztrológiai megfigyelések msgismerésére, vagy a hivatás prediktáló megismerésére

### 1. Szabály alapú predikció:
 > Asztrológógusok tapasztalatai és megfigyelései alapján történik predikció az egyes hivatásokra.
 - A megfigyelések alapján egy általam készített algoritmus segít eldönteni a megfelelő hivatást.
 
### 2. Gépi tanulás alapú predikció:
#### Különböző gépi tanuló algoritmusokkal állítunk fel modelleket, amikből a legjobbat kiválasztva meghatározzuk a baseline-t a mélytanuláshoz
- SGD classifier
- Decision Tree
- K-Fold cross validation
- Logistic Regression
#### Mélytanulás
- A mélyhálók felépítésére Gráf neuronhálóval (graph-attention-network) valósul meg
   - Gráfokban egyszerűbb reprezentálni egy képletet(horoszkópot)
   - Összefüggéseket könnyebben felismerhetjük a tanulás során
- Input réteg: 
   - Bolygó Jegyben analógiák (10)
   - Bolygó Házban analógiák (10)
   - Ház ura Házban analógiák (12)      
   - Ház Jegyben analógiák (12)
   - Fényszögek (12*11) [kapcsolatok a bolygók közt]
- Output réteg
   - %-ban meghatározott esély az egyes hivatásokra
       
#### Hivatások osztályozása:
> Mivel kis adathalmaz áll rendelkezésre, elenite egyszerűbb predikciókat kell tanítani.
- Egyszerű eldöntendő output lehetőségek:
  - Pl.: Irodai munka-e? (az ideális hivatás)

## Megvalósítandó mérföldkövek, funkciók
- [x] horoszkóp szerkezetének implementálása, adatbázisban kezelhetővé tétele ~ 12 hét - 100% KÉSZ
  -  Struktúrára kialakítása, amelyben könnyen kezelhetőek az adatok
- [ ] Adatbázis feltöltése ~ 20 hét - 60% KÉSZ
  - Emberek adatainak beszerzése, strukturált tárolása (~ 400-1000 ember)
  - Analógiák feltöltése: Bolygók, Jegyek, Házak és kombinációik (562 oldal)
- [ ] Pályaválasztás segítő program ~ 15 hét - 35% KÉSZ
  - Neuronhálók segítségével valószínűségi értékek szabása a különböző munkaterületekre a felhasználónak
  - (asztrológia validálására)
- [x] Analógia gyakorló ~ 6 hét - 100% KÉSZ
  - Játékos asztrológia szimbólum tanulási mód
- [x] Általános elemzés ~ 10 hét - 100% KÉSZ
  - Sorstípus: független/kiszolgáltatott/önfeláldozó/áldozat
  - Felosztások: Évszak- Minőség- Elemek- szerinti felosztás
  - Rejtett aszcendens
  - Célkijelölő vagy Megvalósító
  - Hyleg/Anaréta meghatározása
  - Sérült minta Nap/Hold
- [ ] Születési idő pontosítás ~ 12 hét - 25% - KÉSZ
  - Ha egy embernek nem tudjuk pontosan mikor született, de történtek már kardinális események az életében. Vissza lehet számolni, pontosan hány óra hány perckor született.
  - Az analógia gyakorlóhoz hasonló kérdőív kitöltése, ami alapján megtörténik a horoszkóp pontosítás
 
 ### Függőségek:
![IMG_20220512_125512(1)](https://user-images.githubusercontent.com/77636185/176150173-65a703b1-ac58-4d28-9576-b6be4293ad8b.jpg)


## Program 
### Tudnivalók:
 - Backend: Django
 - Adatfeltöltés: python selenium
 - Gépi tanulás: python sklearn
 - Mélytanulás: python tensorflow

### Indítás

#### Dockerrel:
- Docker repository:
`https://hub.docker.com/repository/docker/edom8466/asztro`
- Parancs:
`docker run --name asztro_local -d -p http://127.0.0.1:8006:8000 asztro:latest`
- Indítás:
  - Böngészőbe másolni: `http://127.0.0.1:8006`
  
#### Githubról:
```
git clone https://github.com/molnaredom/asztro.git
pip3 install -r requirements.txt
cd .\weboldal\
python3 .\manage.py makemigrations base
python3 .\manage.py migrate
python3 .\manage.py runserver
```

#### Adatok feltöltése üres adatbázisba
```
python3 adatbazis\webscraping\iranyito.py -m alapadatok
```

## Pár szó magamról:
- Programtervező informatikus szakra járok (4.félév) 
- Szegeden a TTIK-n a Szoftverfejlesztő tanszéken dolgozok. Itt adatok kinyerésével és feldolgozásával foglalkozunk.
- Régebb óta érdekelnek spirituális, pszichológiai dolgok, köztük gyereknevelés, oktatás, absztrakt/elvont gondolkodásmódok, lelki segítségnyújtás, tanulási technikák, tudatalatti, tudatosság. És még ezen kívül sok más.

### Érdeklődni:
- Molnár Ádám
- molnaradam8466@gmail.com

#### Hosszútávú tervek:
- Szövegfeldolgozással kinyerni az analógiáknak az értelmét mesterséges intelligenciával, ezáltal kérdéseket feltenni élethelyzet pontosításhoz.
- Számítógép grafikával létrehozni 3d- képlet modelleket a könyebb értelmezhetőség érdekében

#### *korábbi ötletek(NEM RELEVÁNS MÁR)*
- A személyiségmodellben egyes analógia csoportkörök pont értéket fognak kapni. A megkapott értékek alapján egy optimális küszöbindexet határozunk meg.
Amelyik tulajdonság átlépi a küszöbindexet, belekerül az eredményhalmazba.

- A tulajdonságok közt súlyozott gráfokkal döntjük el a szinonima, ellentettszavak kapcsolatát.(ezek előre definináltak, az alaphalmaz elemei)

