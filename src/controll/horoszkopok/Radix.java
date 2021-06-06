package controll.horoszkopok;

import controll.horoszkopEgysegek.Bolygo;
import controll.horoszkopEgysegek.Fenyszog;
import controll.horoszkopEgysegek.Haz;
import controll.elemzes.AltalanosElemzes;
import modell.analogiak.JegyAnalogia;

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

    public void elemzes() {

        for (Bolygo b : bolygok){
            System.out.println(b.getNev()+" : "+b.getFokszam()+" :  "+b.getJegy().getJegyNev()+" : " +b.getBolygoHazSzama());
        }
        //hazurak kiirasa:
        Arrays.stream(hazak).forEach(e -> AltalanosElemzes.hazUraMelyikHazban(e,bolygok));
        System.out.println();

        JegyAnalogia.randomAnalogia("kos");
        System.out.println();

        AltalanosElemzes.minosegSzerintiFelosztas(bolygok,egyes);

        AltalanosElemzes.elemekSzerintiFelosztas(bolygok,egyes);
        System.out.println();

        AltalanosElemzes.sorstipus(bolygok,hazak);
        System.out.println();

        AltalanosElemzes.hazUraMelyikHazban(kilences,bolygok);
        System.out.println();
        AltalanosElemzes.asztrocikcakk(bolygok);
        System.out.println();


        AltalanosElemzes.hyleg(bolygok);

        AltalanosElemzes.napHoldPluszosMinuszos(bolygok,ferfi);

        AltalanosElemzes.dekadok(bolygok);

        AltalanosElemzes.sorsfeladat(bolygok);

        AltalanosElemzes.bolygokfenyszögei(bolygok);
    }




}
