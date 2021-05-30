package controll.horoszkopok;

import controll.horoszkop.Bolygo;
import controll.horoszkop.Haz;
import modell.analogiak.JegyAnalogia;

import java.util.Arrays;

public class Radix extends Horoszkop {


    public Radix(boolean ferfi, Bolygo nap, Bolygo hold, Bolygo merkur, Bolygo mars, Bolygo venusz, Bolygo jupiter, Bolygo szaturnusz, Bolygo uranusz, Bolygo neptun, Bolygo pluto, Haz egyes, Haz kettes, Haz harmas, Haz negyes, Haz otos, Haz hatos, Haz hetes, Haz nyolcas, Haz kilences, Haz tizes, Haz tizenegyes, Haz tizenkettes) {
        super(ferfi,nap, hold, merkur, mars, venusz, jupiter, szaturnusz, uranusz, neptun, pluto, egyes, kettes, harmas, negyes, otos, hatos, hetes, nyolcas, kilences, tizes, tizenegyes, tizenkettes);
    }

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

        Elemzes.dekadok(bolygok);

        Elemzes.sorsfeladat(bolygok);

        Elemzes.bolygokfenyszögei(bolygok);
    }

    public void fenyszogKapcsLetrehozas(){
        for (Bolygo b : bolygok) {
            double bolygoFok = b.getFokszam();
            String jegyNev = b.getBolygoJegye().getJegyNev();


            //todo ezt altalanos formara hozni hogy minden fenyszogre mukodjon a mellette levo jegyek vizsgalata
            for (Bolygo keres :bolygok) {
                String keresettJegy =keres.getBolygoJegye().getJegyNev();

                //konjukciovizsgálat
                if (keresettJegy.equals(jegyNev) &&
                    Math.abs( bolygoFok-keres.getFokszam())<=10&&
                    keres!=b //a ket bolyg nem ugyanaz
                ) {

                    b.fenyszogKapcsHozzaad("konjukcio",keres.getNev());

                    //elottel levo jegy utolso 10 fokanak vizsgalata
                } else if (b.getBolygoJegye().getMellette()[0].equals(keresettJegy) &&
                        keres.getFokszam()>=20 &&
                        (30-keres.getFokszam()+bolygoFok)<=10) {

                    b.fenyszogKapcsHozzaad("konjukcio",keres.getNev());

                    //utana levo jegy elso 10 fokanak vizsgalata
                } else if (b.getBolygoJegye().getMellette()[1].equals(keresettJegy) &&
                        keres.getFokszam()>=20 &&
                        (keres.getFokszam()+30-bolygoFok)<=10) {

                    b.fenyszogKapcsHozzaad("konjukcio",keres.getNev());

                }

            }







        }
    }

}
