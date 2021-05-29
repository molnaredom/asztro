package controll.horoszkopok;

import controll.horoszkop.Bolygo;
import controll.horoszkop.Haz;
import controll.horoszkop.Jegy;

import java.util.Date;

public class HoroszkopokOsszevetes {

    boolean ferfi;


    Radix radix = new Radix(
            true,
            new Bolygo("nap", new Jegy("oroszlan"), new Haz(8)),
            new Bolygo("hold", new Jegy("szuz"), new Haz(8)),
            new Bolygo("merkur", new Jegy("szuz"), new Haz(8)),
            new Bolygo("mars", new Jegy("nyilas"), new Haz(12)),
            new Bolygo("venusz", new Jegy("rak"), new Haz(7)),
            new Bolygo("jupiter", new Jegy("rak"), new Haz(7)),
            new Bolygo("szaturnusz", new Jegy("ikrek"), new Haz(6)),
            new Bolygo("uranusz", new Jegy("vizonto"), new Haz(2)),
            new Bolygo("neptun", new Jegy("vizonto"), new Haz(1)),
            new Bolygo("pluto", new Jegy("nyilas"), new Haz(12)),

            new Haz(1, new Jegy("bak")),
            new Haz(2, new Jegy("vizonto")),
            new Haz(3, new Jegy("kos")),
            new Haz(4, new Jegy("bika")),
            new Haz(5, new Jegy("bika")),
            new Haz(6, new Jegy("ikrek")),
            new Haz(7, new Jegy("rak")),
            new Haz(8, new Jegy("oroszlan")),
            new Haz(9, new Jegy("merleg")),
            new Haz(10, new Jegy("skorpio")),
            new Haz(11, new Jegy("skorpio")),
            new Haz(12, new Jegy("nyilas"))


    );

    public void szovegesertekeles() {
        radix.elemzes();
    }

    Date datum = new Date();
    //tum.setTime(2001,8,19,15,);

    //LocalDateTime most = new LocalDateTime();



}
