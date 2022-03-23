# Mélytanulási megközelítés:

Az input vektorban diszkrét és numerikus értékek is vannak

Az output vektorban 0-1 közti folytonos számértéket várunk el 
Tehát regressziós a feladat

## Jellemzővektorok Súlyozással:

## paraméterek értelmezése
keras.layer dense - teljesen kapcsolt réteg fully connected (kivéve az egyrétegen belüliek)
optimalizáló RMStrop okosabb mint a gradient decent, de érdemes többet kitalálni
batch méret - 3 megközelítés  
1. egyesével megyünk a példákon , lassú sok számolás, 
2. betöltöm az egész adatbázist, megyek 1 epochot és nem is konvergalok olyn jol
3. földarabolom kötegekre részekre az adatot, és minden 128 példa után összegzek és tanítom a példámat
batch méret mennyi adat legyen egyszerre vizsgálva

epochok száma: legelsotol a legutolsoig vévigment a teljes adatbazis, általában 1 kevés

ha nem azt szaámolom hanyszor menjek végig a teljes adatbázison, akkor azt kell megadni hány frissítés legyen?(20 epochnyi)
ha batch = 128
epoch = 20
frissítések száma = minden batch egy firssítés, egyszer okosabb lett az adatbázis
ha frissítések száma 500 ,akkor az 128*500 adat kell hozzá, az epoch szám itt az adatbázis nyagyságától függ, ha 128*500 az adatbázis méret , akkor pont 1 epochot fut


### Alap adatok
- Nem [diszkrét]
- Kor [numerikus]

###Házak jegyekben
- 1-es ház --- [diszkrét] 5 személyiség, vezetői hajlam
- 2-es ház ---- [diszkrét] 8 pénzügyek
- 3-mas ház --- [diszkrét] 7 kapcsolatok, tudás
- 5-ös ház --- [diszkrét] 9 vállalkozáshajlam
- 6-os ház --- [diszkrét] 10 munkához való viszony
- 7-es ház --- [diszkrét] 5 külvilágban való megnyilvánulás
- 8 as ház --- [diszkrét] 4 kis csapadban való megnyilvánulás
- 9 es ház --- [diszkrét] egyetemek, külföld
- 10 es ház --- [diszkrét] célok
- 11 es ház --- [diszkrét] hivatási munka
- 12 es ház --- [diszkrét] egységben csapatban való dolgozás képessége

### Bolygók jegyekben
- hold[diszkrét]  tehetség
- nap[diszkrét]  kiteljesedési forma
- merkúr[diszkrét]  kommunikációs képesség
- mars [diszkrét] határozottság magabiztosság
- vénusz [diszkrét] pénzhez való viszony

### Bolyok hazakban
- jupiter --- [diszkrét] ahol boldog lehet
- szaturnusz --- [diszkrét] ami irányába menni fog és ami a bukást hozza
- nap --- [diszkrét] ahol kiteljesedik


##Kizárandó megközelítések:
- Döntési fa
  - Mivel a kevésébé fontos jellemzőket elhagyjuk a döntési fáknál ezért elvetjük
  - Pont arra lenne szükség hogy minden szempontot figyelembe vegyünk




# Egyéb megközelítés
- A döntési fákoz hasonló módon 2 irányba ágaztatni a feltételek mentén
  - Pl alkalmas e irodai munkara(erre lefuttatunk egy külön teljes tesztet)
  - Humán vagy reál beállítottsága van (erre is egy külön teljes tesztet)
  - ...Így tovább ágaztatni és mindenre külön futtatni egy algoritmust ami meghatározza alkalmas e valamire