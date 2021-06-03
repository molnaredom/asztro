Asztroprogram 1.1.1

Pár szó magamról: 
-2.féléves programtervező infóra járok
-régebb óta érdekelnek spirituális, pszichológiai dolgok, köztük gyereknevelés, oktatás, absztrakt/elvont gondolkodásmódok, lelki segítségnyújtás, tanulási technikák, tudatalatti, tudatosság. És még ezen kívül sok más. 

A projektemben szeretnék az asztrológia eszközével egy olyan programot készíteni, ami emberek életében segít megfelelő döntéseket hozni az különböző horoszkópok összevetett kiértékelésének  függvényében. 
- [x] horoszkóp szerkezetének implementálása

Mi az asztrológia?
Szimbolikus következtetőrendszer, amiben idő minőségét vizsgáljuk. Másképpen mondva: Egy időpillanat elemzése a felállított szimbolikus bolygóhelyzetek alapján.
Filozófiailag akkor elfogadható az asztrológia, ha elismerjük,hogy nincsenek véletlenek.

A kiértékelt eredmények a következő területeken segíthetnek:
- [] Pályaválasztás
- [] Általános önismeret


Működési vázlat:

1. A kedves emberünk megadja az adatait(neme, szül.hely, szül.idő(év,hónap, nap, óra, perc)). Pontos adatok hiányában nem működik a program.

2. Ezek alapján  készül 3 horoszkóp: (Egész életre vonatkozó(radix), Éves(solar), Holdciklusú(lunar))

-Ezek a program által kiértékelődnek és részletes képet ad a kedves emberünkről.

3. A program feltesz kérdéseket, amivel a kedves emberünk élethelyzetét pontosítjuk.

-A kérdések sorrendjéről, típusáról egy optimalizálási algoritmus fog gondoskodni.
-Mindenki egyénre szabottan kap kérdéseket a kérdésbanból, egyénreszabott sorrendben.
      -Első kérdések ellenőrző,hitelességigazoló jellegűek.
      -Második fázisban a kérdéses életterületet feltérképezzük.
                -A következő kérdés mindig az előző kérdésekre való válaszok reakciójaként keletkezik
      
4. Kiértékelés

- A személyiségmodellben egyes analógia csoportkörök pont értéket fognak kapni. A megkapott értékek alapján egy optimális küszöbindexet határozunk meg.
Amelyik tulajdonság átlépi a küszöbindexet, belekerül az eredményhalmazba.
A tulajdonságok közt súlyozott gráfokkal döntjük el a szinonima, ellentettszavak kapcsolatát.(ezek előre definináltak, az alaphalmaz elemei)

-A kért szolgáltatásnak megfelelő elemzés kiírása.



Érdeklődni: Molnár Ádám molnaradam8466@gmail.com

1.0 2021 marc.30
1.1 2021 maj.31
1.1.1 2020. jun 2.
