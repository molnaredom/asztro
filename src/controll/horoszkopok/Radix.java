package controll.horoszkopok;

import controll.horoszkop.Bolygo;
import controll.horoszkop.Haz;
import modell.analogiak.JegyAnalogia;

import java.util.Arrays;

public class Radix extends Horoszkop {


    public Radix(boolean ferfi, Bolygo nap, Bolygo hold, Bolygo merkur, Bolygo mars, Bolygo venusz, Bolygo jupiter, Bolygo szaturnusz, Bolygo uranusz, Bolygo neptun, Bolygo pluto, Haz egyes, Haz kettes, Haz harmas, Haz negyes, Haz otos, Haz hatos, Haz hetes, Haz nyolcas, Haz kilences, Haz tizes, Haz tizenegyes, Haz tizenkettes) {
        super(ferfi,nap, hold, merkur, mars, venusz, jupiter, szaturnusz, uranusz, neptun, pluto, egyes, kettes, harmas, negyes, otos, hatos, hetes, nyolcas, kilences, tizes, tizenegyes, tizenkettes);
    }
/*
    @Override
    protected Haz[] setHazak(Haz egyes, Haz kettes, Haz harmas, Haz negyes, Haz otos, Haz hatos, Haz hetes, Haz nyolcas, Haz kilences, Haz tizes, Haz tizenegyes, Haz tizenkettes) {
        return new Haz[] {egyes, kettes, harmas, negyes, otos, hatos, hetes, nyolcas, kilences, tizes, tizenegyes, tizenkettes};
    }
*/

    public void elemzes() {
        //hazurak kiirasa:
        Arrays.stream(hazak).forEach(e ->Elemzes.hazUraMelyikHazban(e,bolygok));
        System.out.println();

        JegyAnalogia.randomAnalogia("kos");
        System.out.println();

        Elemzes.minosegSzerintiFelosztas(bolygok,egyes);

        Elemzes.elemekSzerintiFelosztas(bolygok,egyes);
        System.out.println();

        Elemzes.sorstipus(bolygok,hazak);
        System.out.println();

        Elemzes.hazUraMelyikHazban(kilences,bolygok);
        System.out.println();

        Elemzes.asztrocikcakk(bolygok);
        System.out.println();

        Elemzes.hyleg(bolygok);

        Elemzes.napHoldPluszosMinuszos(bolygok,ferfi);



    }

}
