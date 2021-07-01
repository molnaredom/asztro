package controll.emberek;

import controll.horoszkopEgysegek.Bolygo;
import controll.horoszkopEgysegek.Haz;
import controll.horoszkopEgysegek.Jegy;
import controll.horoszkopok.Radix;

import java.util.List;

public class Ember {


    List<String[]> adatok;

    public Ember(String nev) {
        this.adatok = Beolvas.beolv(nev);
    }




    public void szovegesertekeles() {

        try {
            Radix radix = new Radix(
                    true,
                    //todo read bolygok from file
                    new Bolygo("nap", new Jegy(adatok.get(0)[0]), Double.parseDouble(adatok.get(0)[1])),
                    new Bolygo("hold", new Jegy(adatok.get(1)[0]), Double.parseDouble(adatok.get(1)[1])),
                    new Bolygo("merkur", new Jegy(adatok.get(2)[0]), Double.parseDouble(adatok.get(2)[1])),
                    new Bolygo("mars", new Jegy(adatok.get(3)[0]), Double.parseDouble(adatok.get(3)[1])),
                    new Bolygo("venusz", new Jegy(adatok.get(4)[0]), Double.parseDouble(adatok.get(4)[1])),
                    new Bolygo("jupiter", new Jegy(adatok.get(5)[0]), Double.parseDouble(adatok.get(5)[1])),
                    new Bolygo("szaturnusz", new Jegy(adatok.get(6)[0]), Double.parseDouble(adatok.get(6)[1])),
                    new Bolygo("uranusz", new Jegy(adatok.get(7)[0]), Double.parseDouble(adatok.get(7)[1])),
                    new Bolygo("neptun", new Jegy(adatok.get(8)[0]), Double.parseDouble(adatok.get(8)[1])),
                    new Bolygo("pluto", new Jegy(adatok.get(9)[0]), Double.parseDouble(adatok.get(9)[1])),

                    new Haz("1", new Jegy(adatok.get(10)[0]), Double.parseDouble(adatok.get(10)[1])),
                    new Haz("2", new Jegy(adatok.get(11)[0]), Double.parseDouble(adatok.get(11)[1])),
                    new Haz("3", new Jegy(adatok.get(12)[0]), Double.parseDouble(adatok.get(12)[1])),
                    new Haz("4", new Jegy(adatok.get(13)[0]), Double.parseDouble(adatok.get(10)[1])),
                    new Haz("5", new Jegy(adatok.get(14)[0]), Double.parseDouble(adatok.get(11)[1])),
                    new Haz("6", new Jegy(adatok.get(15)[0]), Double.parseDouble(adatok.get(12)[1])),
                    new Haz("7", new Jegy(adatok.get(16)[0]), Double.parseDouble(adatok.get(10)[1])),
                    new Haz("8", new Jegy(adatok.get(17)[0]), Double.parseDouble(adatok.get(11)[1])),
                    new Haz("9", new Jegy(adatok.get(18)[0]), Double.parseDouble(adatok.get(12)[1])),
                    new Haz("1", new Jegy(adatok.get(19)[0]), Double.parseDouble(adatok.get(10)[1])),
                    new Haz("1", new Jegy(adatok.get(20)[0]), Double.parseDouble(adatok.get(11)[1])),
                    new Haz("1", new Jegy(adatok.get(21)[0]), Double.parseDouble(adatok.get(12)[1]))
            );

            radix.alapbeallitasok();
            radix.osszefuggesElemzes();
            //radix.bolygoJegybenElemzes();



        } catch (IndexOutOfBoundsException ie) {
            System.err.println("Kevés adatot vittél be");
        } catch (NumberFormatException ne) {
            System.err.println("Szám helyett valami más adatot adtál meg");
        }


    }


}
