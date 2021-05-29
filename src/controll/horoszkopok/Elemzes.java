package controll.horoszkopok;

import controll.horoszkop.Bolygo;
import controll.horoszkop.Haz;
import modell.analogiak.HazAnalogia;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public interface Elemzes {


    //todo lesz egy összetett adattipus ami kulonbozo ertekeket tarol int pl (1,10,32,21,24)
    //todo es ez minden elemzes interfaceban levo fuggbeny visszateresi ertek lesz
    // majd a visszateritett ertekeket  a horoszlkoposszesito classban kiértékeli és egy összetett szemelyiseget alkot majd

    boolean vanhazur = false;


    //személyiség
    static void evszakiFelosztas(Bolygo[] bolygok) {
    int tavasz = 0, tel = 0, nyar = 0, osz = 0;


    for (Bolygo k : bolygok) {
        switch (k.getBolygoJegye().getEvszak()) {
            case "tavasz" -> tavasz += k.getPont();
            case "nyar" -> nyar += k.getPont();
            case "osz" -> osz += k.getPont();
            case "tel" -> tel += k.getPont();
        }
    }

    System.out.printf("tavasz:%d\nnyar:%d\nosz:%d\ntel:%d%n",tavasz,nyar,osz,tel);
}

    static void dekadok(Bolygo[] bolygok) {



        for (Bolygo b : bolygok) {
            System.out.println("bolygo: "+b.getNev() +" fokszam: "+b.getFokszam() + " dekadszam: "+b.getDekadSzam() );
            System.out.println("||-->> "+b.getDekadJegy());

        }

    }


    static void minosegSzerintiFelosztas(Bolygo[] bolygos, Haz asc) {

        int kardinalis=0, szilard=0, valtozo=0;


        for (Bolygo b : bolygos) {

            switch (b.getBolygoJegye().getMinoseg()) {
                case "kardinalis" -> kardinalis += b.getPont();
                case "szilard" -> szilard += b.getPont();
                case "valtozo" -> valtozo += b.getPont();
            }
        }
        switch (asc.getHazJegye().getMinoseg()) {
            case "kardinalis" -> kardinalis += 2;
            case "szilard" -> szilard += 2;
            case "valtozo" -> valtozo += 2;
        }


        System.out.printf("kardinalis:%d\nszilard:%d\nvaltozo:%d\n",kardinalis,szilard,valtozo);
    }


    static void elemekSzerintiFelosztas(Bolygo[] bolygos, Haz asc) {

        int tuz=0, viz=0, fold=0, levego=0;

        for (Bolygo b : bolygos) {

            switch (b.getBolygoJegye().getElem()) {
                case "tuz" -> tuz += b.getPont();
                case "fold" -> fold += b.getPont();
                case "levego" -> levego += b.getPont();
                case "viz" -> viz += b.getPont();
            }
        }
        switch (asc.getHazJegye().getElem()) {
            case "tuz" -> tuz += 2;
            case "fold" -> fold += 2;
            case "levego" -> levego += 2;
            case "viz" -> viz += 2;
        }


        System.out.printf("tuz:%d\nfold:%d\nlevego:%d\nviz:%d",tuz,fold,levego,viz);
    }




    //sors
    static void asztrocikcakk(Bolygo[] bolygok) {
        //ArrayList<String> jegybenEles = new ArrayList<>(Arrays.asList("szaturnusz","uranusz","nap"));
        ArrayList<String> hazbanEles = new ArrayList<>(Arrays.asList("neptun","jupiter","pluto"));

        //elso parameter: hazszam vagy jegy , masodik: maga a bolygo
        HashMap<String,String> parositas = new HashMap<>();

        for (String hazbanEltBolygo : hazbanEles) {
            for (Bolygo b : bolygok) {
                if (b.getNev().equals(hazbanEltBolygo)) {
                    parositas.put(b.getNev(),String.valueOf(b.getBolygoHaza().getHazszam()));
                }
            }
        }
        parositas.put("szaturnusz",bolygok[6].getBolygoJegye().getJegyNev());
        parositas.put("uranusz",bolygok[7].getBolygoJegye().getJegyNev());
        parositas.put("nap",bolygok[0].getBolygoJegye().getJegyNev());

        System.out.printf("""
                %s szaturnusz  ------->  neptun a %s. házban
                                        ______-'
                %s uránusz    <---'
                         '------------->  jupiter a %s. házban
                                     ______-'
                %s nap     <---'
                        '------------->     plutó a %s. házban   
                """,parositas.get("szaturnusz"),parositas.get("neptun"),parositas.get("uranusz"),
                parositas.get("jupiter"),parositas.get("nap"),parositas.get("pluto"));





    }


    static void sorstipus(Bolygo[] bolygok, Haz[] hazak){

        ArrayList<Integer> kiemeltHazak = new ArrayList<>(Arrays.asList(1,5,9,10,11));

        boolean onfelaldozo = false; //ha false akkor kiszolgaltatott

        int uranuszHazszam = bolygok[7].getBolygoHaza().getHazszam();
        int neptunHazszam = bolygok[8].getBolygoHaza().getHazszam();
        int jupiterHazszam = bolygok[5].getBolygoHaza().getHazszam();
        int szaturnHazszam = bolygok[6].getBolygoHaza().getHazszam();

        //nap hold...venusz +pluto
        Bolygo[] pontoteroBolygok = Arrays.copyOfRange(bolygok,0,6);//elso 6 bolygot veszi
        pontoteroBolygok[5] = bolygok[bolygok.length-1]; //jupitert kicsereli a plutora

        //sorstipus donto controll.hazak pontszama
        int p12 =0;
        int p11 =0;

        for (Bolygo b : pontoteroBolygok) {
            if (b.getBolygoHaza().getHazszam()==12) p12+=b.getPont();
            else if (b.getBolygoHaza().getHazszam()==11) p11+= b.getPont();
        }

        int vizonto=0;
        int halak =0;

        for (Bolygo b : pontoteroBolygok) {
            if (b.getBolygoJegye().getJegyNev().equals("vizonto")) vizonto+= b.getPont();
            else if (b.getBolygoJegye().getJegyNev().equals("halak")) halak+= b.getPont();
        }


        if (kiemeltHazak.contains(uranuszHazszam) && !kiemeltHazak.contains(neptunHazszam)){
            System.out.println("Elsőkörös Uránuszi = választhat- független vagy kiszolgáltatott");
            onfelaldozo = false;
        }
        else if (!kiemeltHazak.contains(uranuszHazszam) && kiemeltHazak.contains(neptunHazszam)) {
            System.out.println("Első körös neptuni = választhat- áldozat vagy önfeláldozó");
            onfelaldozo = true;
        }
        else if (!kiemeltHazak.contains(jupiterHazszam) && kiemeltHazak.contains(szaturnHazszam)){
            System.out.println("Második körös vegyes kiszolgáltatott");
            onfelaldozo = false;
        }
        else if (kiemeltHazak.contains(jupiterHazszam) && !kiemeltHazak.contains(szaturnHazszam)){
            System.out.println("Második körös vegyes önfeláldozó");
            onfelaldozo = true;
        }
        else if (p11>p12) {
            System.out.println("Haramdik körös vegyes kiszolgáltatott");
            onfelaldozo = false;
        }
        else if (p12>p11) {
            System.out.println("Haramdik körös vegyes önfeláldozó");
            onfelaldozo = true;
        }
        else if(vizonto<halak)  {
            System.out.println("Negyedik körös vegyes önfeláldozó");
            onfelaldozo = true;
        }
        else if(vizonto>halak)  {
            System.out.println("Negyedik körös vegyes kiszolgáltatott");
            onfelaldozo = false;
        }else {
            System.out.println("5. köröst még nem tudjuk meghatározni");
        }
        //todo otodik kort megcsinalni --fenyszoges feladat


        if (onfelaldozo) {
            //Haz halakHaza = (Arrays.stream(controll.hazak).filter(e->e.getJegyHazban().getNev().equals("halak")).findFirst().orElse(null));


            //assert halakHaza != null;
            System.out.println("le kell mondania egyről a következők közül:\n" +
                    "a neptun házának analógiáiról: "+ Arrays.toString(HazAnalogia.hazak[neptunHazszam - 1]) +
                    "\n a jupiter házának analógiáiról: "+ Arrays.toString(HazAnalogia.hazak[jupiterHazszam - 1])+
                    "\n a szaturnusz házának analógiák: "+ Arrays.toString(HazAnalogia.hazak[szaturnHazszam - 1])+
                    "\n ahol a halak jegye kezdődik: "
                   // + Arrays.toString(HazAnalogia.controll.hazak[halakHaza.getHazszam()])
            );

        } else {
            //Haz vizontoHaza = (Arrays.stream(controll.hazak).filter(e->e.getJegyHazban().getNev().equals("vizonto")).findFirst().orElse(null));
            //assert vizontoHaza != null;
            System.out.println("kiszogláltatottsáhot kell megélnie az egyikből a következők közül:\n" +
                    "az uránusz házának analógiák: "+ Arrays.toString(HazAnalogia.hazak[uranuszHazszam - 1]) +
                    "\n a jupiter házának analógiáiról: "+ Arrays.toString(HazAnalogia.hazak[jupiterHazszam - 1])+
                    "\n a szaturnusz házának analógiák: "+ Arrays.toString(HazAnalogia.hazak[szaturnHazszam - 1])+
                    "\n a vízöntő jegyében álló bolygók analógiák: "
                    //+ Arrays.toString(HazAnalogia.controll.hazak[vizontoHaza.getHazszam()])
            );
        }
        //todo bolygo egyuttallasok alapjan levo sorsmegelesi lehetosegek




    }


    static void sorsfeladat(Bolygo[] bolygok) {
        Bolygo szaturn = bolygok[6];
        Bolygo jupi = bolygok[5];

    }





    // egyéb
    static void hyleg(Bolygo[] bolygok) {
        int napHaza = bolygok[0].getBolygoHaza().getHazszam();
        int holdHaza = bolygok[1].getBolygoHaza().getHazszam();
        ArrayList<Integer> kiemeltHazak = new ArrayList<>(Arrays.asList(7,9,10,11));

        if(kiemeltHazak.contains(napHaza) ){
            System.out.println("hyleg a nap"+ napHaza + ". hazban");
        } else if (kiemeltHazak.contains(holdHaza)) {
            System.out.println("hyleg a hold a "+ holdHaza + ". hazban");
        }else {
            System.out.println("hyleg az ASC");
        }



    }


    static void megvalVcelkij(Bolygo[] bolygok, Haz[] hazak) {
        int cel =0;
        int megv =0;

        if (vaneHazur(hazak[0],bolygok)) megv++;
        if (vaneHazur(hazak[9],bolygok)) cel++;

        //if (tamadva)
        //todo megnezni tamadja e az mct vagy za asct kvadrat vagy oppozicio ez alapjan pontot adni

        if (megv==cel) {
            //todo megvizsgalni a marsot tamadjak e es eldonteni veglegesen
        }
        //todo eldonteni celk, vagy megvalosito e?

    }

    static boolean vaneHazur(Haz haz, Bolygo[] bolygok) {

        boolean vanHazur = false;

        for (Bolygo b : bolygok) {
            if( b.getNev().equals(haz.hazUralkodoBolygoja()) ) {

                if (b.getBolygoJegye().isPozitiv() == haz.getHazJegye().isPozitiv()
                    //||
                    //          b.getBolygoJegye().isPozitiv() != haz.getJegyHazban().isPozitiv() && b.
                ) {
                    return true;
                }
            }
        }
        return false;

    }


    static void hazUraMelyikHazban(Haz haz, Bolygo[] bolygok) {

        boolean vanHazur = false;

        for (Bolygo b : bolygok) {
            if( b.getNev().equals(haz.hazUralkodoBolygoja()) ) {

                if (b.getBolygoJegye().isPozitiv() == haz.getHazJegye().isPozitiv()
                        //||
                    //          b.getBolygoJegye().isPozitiv() != haz.getJegyHazban().isPozitiv() && b.
                ) {
                    vanHazur=true;
                    System.out.printf("%d-s ura a %d-sben\n",haz.getHazszam(), b.getBolygoHaza().getHazszam());
                }

            }

        }
        if (!vanHazur) {
            System.out.println("Nincs házúr: "+haz.getHazszam());
            System.out.printf("Tagadni fogja a %s jegy analógiáit %d ház területén, úgy hogy megtartsa a %s analógiákat.\n",
                    haz.getHazJegye().getOpposit(),haz.getHazszam(),haz.getHazJegye().getJegyNev());

        }

    }


    static void napHoldPluszosMinuszos(Bolygo[] bolygok, boolean ferfi) {
        int napHaza = bolygok[0].getBolygoHaza().getHazszam();
        int holdHaza = bolygok[1].getBolygoHaza().getHazszam();

        ArrayList<Integer> kiemeltVilagosHazak = new ArrayList<>(Arrays.asList(1,5,9,10,11));
        ArrayList<Integer> kiemeltSotetHazak = new ArrayList<>(Arrays.asList(4,8,12));


        if (!ferfi) { // akkor nő
            if (kiemeltVilagosHazak.contains(napHaza)) {
                System.out.println("plusz napos");
                System.out.println("a hold szerepek nap szerepen keresztül jelennek meg\n" +
                        "pl gyereket nevel, de nap szerepen keresztül, pl egyedül neveli, ő irányítja a családot");
            }
            if (kiemeltSotetHazak.contains(holdHaza)) {
                System.out.println("minusz holdas");
                System.out.println("problémás a hold szerepek felvállalása, így célszerű a külvilágban megélnie a holdat");
                // todo ha konj, kvad, trigon, opoz fenyszog eri a holdat a marstol vagy a jupiteről akk is min holdas
            }
        } else {
            if (kiemeltSotetHazak.contains(napHaza)) {
                System.out.println("minusz napos");
                System.out.println("a vesztés szimbólum analógiáin keresztül lehet nap\n" +
                        "pl bajbajutott embereken segít , így ő nap lesz, ha nem máson keresztül éli akkor a saját bőrén");
                //todo ugyanigy kiegesziteni
            }
            if (kiemeltVilagosHazak.contains(holdHaza)) {
                System.out.println("plusz holdas");
                System.out.println("csak a hold analógiákon keresztül lehet nap" +
                        "\n pl hold közegben ő az irányító");

            }


        }



    }

}

