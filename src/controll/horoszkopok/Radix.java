package controll.horoszkopok;

import controll.horoszkop.Bolygo;
import controll.horoszkop.Haz;
import controll.horoszkopok.elemzes.AltalanosElemzes;
import modell.analogiak.JegyAnalogia;

import java.util.Arrays;

public class Radix extends Horoszkop {


    public Radix(boolean ferfi, Bolygo nap, Bolygo hold, Bolygo merkur, Bolygo mars, Bolygo venusz, Bolygo jupiter, Bolygo szaturnusz, Bolygo uranusz, Bolygo neptun, Bolygo pluto, Haz egyes, Haz kettes, Haz harmas, Haz negyes, Haz otos, Haz hatos, Haz hetes, Haz nyolcas, Haz kilences, Haz tizes, Haz tizenegyes, Haz tizenkettes) {
        super(ferfi,nap, hold, merkur, mars, venusz, jupiter, szaturnusz, uranusz, neptun, pluto, egyes, kettes, harmas, negyes, otos, hatos, hetes, nyolcas, kilences, tizes, tizenegyes, tizenkettes);
    }

    public void elemzes() {
        //hazurak kiirasa:
        /*Arrays.stream(hazak).forEach(e -> AltalanosElemzes.hazUraMelyikHazban(e,bolygok));
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
*/
        AltalanosElemzes.bolygokfenyszögei(bolygok);
    }

    public void fenyszogKapcsLetrehozas(){
        for (Bolygo b : bolygok) {

            for (Bolygo keres :bolygok) {

                //konjukciovizsgálat
                konjukcio(b,keres,"konjukcio");
                oppozicio(b,keres,"oppozicio");
                kvadrat(b,keres,"kvadrat");

            }
        }
    }

    /**segedfuggveny bolygot vár aminek visszza adja a jegynevét*/
    private String jegynev(Bolygo bolygo) {
        return bolygo.getBolygoJegye().getJegyNev();
    }



    public void konjukcio(Bolygo b, Bolygo keres, String fenyszogNev) {

        double bolygoFok = b.getFokszam();


        if (keres.getBolygoJegye().getJegyNev().equals(b.getBolygoJegye().getJegyNev()) &&
                Math.abs( bolygoFok-keres.getFokszam())<=10&&
                keres!=b //a ket bolyg nem ugyanaz
        ) {

            b.fenyszogKapcsHozzaad(fenyszogNev,keres.getNev());

            //elottel levo jegy utolso 10 fokanak vizsgalata
        } else if (keres.getBolygoJegye().getJegyNev().equals(b.getBolygoJegye().getMellette()[0]) &&
                keres.getFokszam()>=20 &&
                (30-keres.getFokszam()+bolygoFok)<=10) {

            b.fenyszogKapcsHozzaad(fenyszogNev,keres.getNev());

            //utana levo jegy elso 10 fokanak vizsgalata
        } else if (keres.getBolygoJegye().getJegyNev().equals(b.getBolygoJegye().getMellette()[1]) &&
                keres.getFokszam()<=10 &&
                (keres.getFokszam()+30-bolygoFok)<=10) {

            b.fenyszogKapcsHozzaad(fenyszogNev,keres.getNev());

        }
    }

    public void oppozicio(Bolygo b, Bolygo keres, String fenyszogNev) {

        double bolygoFok = b.getFokszam();


        if (keres.getBolygoJegye().getJegyNev().equals(opposit( b.getBolygoJegye().getJegyNev())) &&
                Math.abs( bolygoFok-keres.getFokszam())<=10&&
                keres!=b //a ket bolyg nem ugyanaz
        ) { b.fenyszogKapcsHozzaad(fenyszogNev,keres.getNev());}

        //elottel levo jegy utolso 10 fokanak vizsgalata
        else if (keres.getBolygoJegye().getJegyNev().equals(opposit(b.getBolygoJegye().getMellette()[0])) &&
                keres.getFokszam()>=20 &&
                (30-keres.getFokszam()+bolygoFok)<=10
        ) { b.fenyszogKapcsHozzaad(fenyszogNev,keres.getNev()); }

        //utana levo jegy elso 10 fokanak vizsgalata
        else if (keres.getBolygoJegye().getJegyNev().equals(opposit(b.getBolygoJegye().getMellette()[1])) &&
                keres.getFokszam()<=10 &&
                (keres.getFokszam()+30-bolygoFok)<=10
        ) { b.fenyszogKapcsHozzaad(fenyszogNev,keres.getNev()); }
    }

    public void kvadrat(Bolygo b1, Bolygo b2, String fenyszogNev) {


        double bolygoFok = b1.getFokszam();

        //bal kvadrat
        if (jegynev(b1).equals(kvad( jegynev(b2))[0]) &&
                Math.abs( bolygoFok-b2.getFokszam())<=10&&
                b2!=b1
        ) { b1.fenyszogKapcsHozzaad(fenyszogNev,b2.getNev()); }

        //JOBB KVADRAT
        else if (jegynev(b1).equals(kvad( jegynev(b2))[1])&&
                Math.abs( bolygoFok-b2.getFokszam())<=10&&
                b2!=b1)
        {
           // System.out.println(kvad(jegynev(b2))[1]);
            b1.fenyszogKapcsHozzaad(fenyszogNev,b2.getNev()); }

        //elottel levo jegy utolso 10 fokanak vizsgalata
        //bal kvadrat - balra jegy
        else if (jegynev(b1).equals(kvad(b2.getBolygoJegye().getMellette()[0])[0]) &&
                b2.getFokszam()>=20 &&
                (30-b2.getFokszam()+bolygoFok)<=10&&
                b2!=b1
        ) { b1.fenyszogKapcsHozzaad(fenyszogNev,b2.getNev());}

        //jobb kvadrat - balra jegy
        else if (jegynev(b1).equals(kvad(b2.getBolygoJegye().getMellette()[0])[1]) &&
                b2.getFokszam()>=20 &&
                (30-b2.getFokszam()+bolygoFok)<=10&&
                b2!=b1
        ) { b1.fenyszogKapcsHozzaad(fenyszogNev,b2.getNev());}

        //utana levo jegy elso 10 foka
        //bal kvadrat jobbra jegy
        else if (jegynev(b1).equals(kvad(b2.getBolygoJegye().getMellette()[1])[0]) &&
                b2.getFokszam()<=10 &&
                (b2.getFokszam()+30-bolygoFok)<=10&&
                b2!=b1
        ) { b1.fenyszogKapcsHozzaad(fenyszogNev,b2.getNev()); }

        //bal kvadrat jobbra jegy
        else if (jegynev(b1).equals(kvad(b2.getBolygoJegye().getMellette()[1])[1]) &&
                b2.getFokszam()<=10 &&
                (b2.getFokszam()+30-bolygoFok)<=10&&
                b2!=b1
        ) { b1.fenyszogKapcsHozzaad(fenyszogNev,b2.getNev()); }
    }




    public String opposit(String atforditandoJegy){
        switch (atforditandoJegy) {
            case "kos" -> { return "merleg"; }
            case "bika" -> { return "skorpio"; }
            case "ikrek" -> { return "nyilas"; }
            case "rak" -> { return "bak"; }
            case "oroszlan" -> { return "vizonto"; }
            case "szuz" -> { return "halak"; }
            case "merleg" -> { return "kos"; }
            case "skorpio" -> { return "bika"; }
            case "nyilas" -> { return "ikrek"; }
            case "bak" -> {return "rak";}
            case "vizonto" -> { return "oroszlan"; }
            case "halak" -> { return "szuz"; }
        }
        return null;
    }

    public String[] kvad(String atforditandoJegy) {
        String[] visszater = new String[2];

        switch (atforditandoJegy) {
            case "kos" : {
                visszater[0] = "rak";
                visszater[1] = "bak";return visszater;

            }
            case "bika" : {
                visszater[0] = "oroszlan";
                visszater[1] = "vizonto";return visszater;
            }
            case "ikrek" : {
                visszater[0] = "szuz";
                visszater[1] = "halak";return visszater;
            }
            case "rak" : {
                visszater[0] = "merleg";
                visszater[1] = "kos";return visszater;
            }
            case "szuz" : {
                visszater[0] = "nyilas";
                visszater[1] = "ikrek";return visszater;
            }
            case "oroszlan" : {
                visszater[0] = "skorpio";
                visszater[1] = "bika";
                return visszater;
            }
            case "merleg" : {
                visszater[0] = "bak";
                visszater[1] = "rak";return visszater;
            }
            case "skorpio" : {
                visszater[0] = "vizonto";
                visszater[1] = "oroszlan";return visszater;
            }
            case "nyilas" : {
                visszater[0] = "halak";
                visszater[1] = "szuz";return visszater;
            }
            case "bak" : {
                visszater[0] = "kos";
                visszater[1] = "merleg";return visszater;
            }
            case "vizonto" : {
                visszater[0] = "bika";
                visszater[1] = "skorpio";return visszater;
            }
            case "halak" : {
                visszater[0] = "ikrek";
                visszater[1] = "nyilas";return visszater;
            }
        }
        return visszater;
    }



}
