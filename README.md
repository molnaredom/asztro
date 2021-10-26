Asztroprogram 2.0.0

Pár szó magamról: 
- 3.féléves programtervező infóra járok
- Szegeden a TTIK-n a Szoftverfejlesztő tanszéken dolgozok. Itt adatok kinyerésével és feldolgozásával foglalkozunk.
- Régebb óta érdekelnek spirituális, pszichológiai dolgok, köztük gyereknevelés, oktatás, absztrakt/elvont gondolkodásmódok, lelki segítségnyújtás, tanulási technikák, tudatalatti, tudatosság. És még ezen kívül sok más. 

Mi az asztrológia?
- Szimbolikus következtetőrendszer, amiben idő minőségét vizsgáljuk. Tulajdonképpen egy időpillanat elemzéséről van szó, emire különböző szimbólumoket helyezve, különböző következtetésekre juthatunk.
- A következő képlet, az égbolt vázlatos rajza egy adott pillanatban, ebből tudunk adatokat kinyerni.
![kép](https://user-images.githubusercontent.com/77636185/138847759-e8614944-8984-4bd0-b738-eafbf976cd1e.png)

Cél:
- A projektemben szeretnék az informatika és az asztrológia vegyítésével egy olyan programot létrehozni, ami különböző módokon segíti előre a használó életét, legfőképpen életvezetési tanácsadás szempontjából.
- Mivel az asztrológiában rengeteg különböző csoportot tudunk megkülönböztetni(Csillagjegyek(12), Házak(12), Bolgyók(10), Fényszögek(~6)) és ezeknek vehetjük kombinációit is(amik megfigyelséek alapján különböző életterületek megoldására utalnak, mutatnak) ,így a mesterséges intelligencia ezen belül is a neuronhálók eszközét könnyen eszközül vehetjük. 
Az asztrológiában sok adat van , sok megfigyelési szempont, egy ember nehezen képes egyszerre ilyen sok szempontot figyelembevenni és objektíven(úgy hogy ne csak a szempontok egy kisebb részhalmaza alapján döntsön) választ adni egy kérdésre.
Cél lenne, hogy felmutassunk hogy mennyire tuja jól megjósolni a program az illető leendő munhahelyének valósínűségeit. Van-e erős korrelácó?


Mérföldkövek alap implementációkban
- [x] horoszkóp szerkezetének implementálása(javíításra szorul)
- [ ] adatbázis feltöltése megfelelő analógiákkal(folyamatban...)
- [ ] weboldal létrehozása ahonnan elérhetőek az információk(folyamatban..)


Mérföldkövek a konkrét elérendő cél tekintetében
- [ ] Pályaválasztás(munka, életút)
- [x] Általános önismeret(javításra szorul)
- [ ] Párkapcsolati elemzés


Működési vázlat:

1.a A kedves emberünk megadja az adatait(neme, szül.hely, szül.idő(év,hónap, nap, óra, perc)). Pontos adatok hiányában nem működik a program.

1.b (opcionális). A program feltesz kérdéseket, amivel a kedves emberünk élethelyzetét pontosítjuk.

2. Ezek alapján  készül 3 horoszkóp: (Egész életre vonatkozó(radix), Éves(solar), Holdciklusú(lunar))
      
3.a Pályaválasztási kiértékelés
Mély neuronháló alkalmazásával dolgozunk.
- Input rétegben megkapja a különböző szempontok analógiáit(6 os ház jegye, hold jegye, 6 os ház ura, 5. ös ház, 3 mas ház, 9 es ház...stb)
- Output rétegen a különböző munkákra fog jósolni a gépünk egy-egy valószínűségi százalékot(pl 0.26- cégvezetői munka, 0.80 hogy irodai alkalmazott...stb)

3.b Párkapcsolati elemzés
- (túl bonyolult, először jussunk el 3.a-ig)

3.c Önismereti fejlesztés
- Általános adatok kiítása(ebben nincs semmi matematika, de mégis személyreszabott, az asztrológia eszköze miatt)


Érdeklődni: 
- Molnár Ádám 
- molnaradam8466@gmail.com 

A terv fejlődési pontjai:
- 1.0.0 2021 marc.30
- 1.1.0 2021 maj.31
- 1.1.1 2021. jun 2.
- 1.1.2 2021 jun 6.
- 2.0.0 2021 okt. 26

korábbi ötletek(NEM RELEVÁNS MÁR)
- A személyiségmodellben egyes analógia csoportkörök pont értéket fognak kapni. A megkapott értékek alapján egy optimális küszöbindexet határozunk meg.
Amelyik tulajdonság átlépi a küszöbindexet, belekerül az eredményhalmazba.

- A tulajdonságok közt súlyozott gráfokkal döntjük el a szinonima, ellentettszavak kapcsolatát.(ezek előre definináltak, az alaphalmaz elemei)




