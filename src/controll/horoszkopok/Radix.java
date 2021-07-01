package controll.horoszkopok;

import controll.elemzes.altalansoelemzes.BolygojegybenElemzes;
import controll.horoszkopEgysegek.Bolygo;
import controll.horoszkopEgysegek.Fenyszog;
import controll.horoszkopEgysegek.Haz;
import controll.elemzes.altalansoelemzes.Osszefugges_elemzes;
import modell.analogiak.alapAnalogiak.JegyAnalogia;

import java.util.Arrays;

public class Radix extends Horoszkop {
    Fenyszog fenyszog = new Fenyszog();

    public Radix(boolean ferfi, Bolygo nap, Bolygo hold, Bolygo merkur, Bolygo mars, Bolygo venusz, Bolygo jupiter, Bolygo szaturnusz, Bolygo uranusz, Bolygo neptun, Bolygo pluto, Haz egyes, Haz kettes, Haz harmas, Haz negyes, Haz otos, Haz hatos, Haz hetes, Haz nyolcas, Haz kilences, Haz tizes, Haz tizenegyes, Haz tizenkettes) {
        super(ferfi, nap, hold, merkur, mars, venusz, jupiter, szaturnusz, uranusz, neptun, pluto, egyes, kettes, harmas, negyes, otos, hatos, hetes, nyolcas, kilences, tizes, tizenegyes, tizenkettes);
    }

    public void alapbeallitasok(){
        fenyszog.fenyszogKapcsLetrehozas(bolygok);
        fenyszog.beallitBolygonakHazat(hazak,bolygok);
    }

    public void osszefuggesElemzes() {

        Osszefugges_elemzes oszfgelemz = new Osszefugges_elemzes(bolygok,hazak,ferfi);

        /*for (Bolygo b : bolygok){
            System.out.println(b.getNev()+" : "+b.getFokszam()+" :  "+b.getJegy().getJegyNev()+" : " +b.getBolygoHazSzama());
        }*/
        //hazurak kiirasa:
        Arrays.stream(hazak).forEach(oszfgelemz::hazUraMelyikHazban);
        System.out.println();

        JegyAnalogia.randomAnalogia("kos");  System.out.println("\n");
        oszfgelemz.minosegSzerintiFelosztas();          System.out.println("\n");
        oszfgelemz.elemekSzerintiFelosztas();           System.out.println("\n");
        oszfgelemz.sorstipus();                         System.out.println("\n");
        oszfgelemz.asztrocikcakk();                     System.out.println("\n");
        oszfgelemz.hyleg();                             System.out.println("\n");
        oszfgelemz.napHoldPluszosMinuszos();            System.out.println("\n");
        oszfgelemz.dekadok();                           System.out.println("\n");
        oszfgelemz.sorsfeladat();                       System.out.println("\n");
        oszfgelemz.bolygokfenyszögei();                 System.out.println("\n");
    }

    public void bolygoJegybenElemzes() {

        BolygojegybenElemzes.bolygoJegybenElemzesKiirat(bolygok);

    }




}
