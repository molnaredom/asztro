package controll.emberek;

import controll.horoszkopEgysegek.Bolygo;
import controll.horoszkopEgysegek.Haz;
import controll.horoszkopEgysegek.Jegy;
import controll.horoszkopok.Radix;

import java.util.Date;
import java.util.Scanner;

public class Ember {

    Date szuletes = new Date();

    Scanner sc = new Scanner(System.in);

    Radix radix = new Radix(
            true,
            //todo read bolygok from file
            new Bolygo(sc.next(), new Jegy("oroszlan"),26.4128),
            new Bolygo("hold", new Jegy("szuz"),3.4952),
            new Bolygo("merkur", new Jegy("szuz"),9.5313),
            new Bolygo("mars", new Jegy("nyilas"),21.06),
            new Bolygo("venusz", new Jegy("rak"),21.03),
            new Bolygo("jupiter", new Jegy("rak"),7.46),
            new Bolygo("szaturnusz", new Jegy("ikrek"),13.40),
            new Bolygo("uranusz", new Jegy("vizonto"),22.41),
            new Bolygo("neptun", new Jegy("vizonto"),6.50),
            new Bolygo("pluto", new Jegy("nyilas"), 12.32),

            //new Bolygo("ASC", new Jegy("bak"), new Haz(1),3.19),
            //new Bolygo("MC", new Jegy("skorpio"), new Haz(10),3.42),

            new Haz("1", new Jegy("bak"),3.3812),
            new Haz("2", new Jegy("vizonto"),17.4210),
            new Haz("3", new Jegy("kos"),2.17),
            new Haz("4", new Jegy("bika"),4.01),
            new Haz("5", new Jegy("bika"),26.37),
            new Haz("6", new Jegy("ikrek"),15.13),
            new Haz("7", new Jegy("rak"),3.3812),
            new Haz("8", new Jegy("oroszlan"),17.4210),
            new Haz("9", new Jegy("merleg"),2.17),
            new Haz("10", new Jegy("skorpio"),4.01),
            new Haz("11", new Jegy("skorpio"),26.37),
            new Haz("12", new Jegy("nyilas"),15.13)


    );




}
