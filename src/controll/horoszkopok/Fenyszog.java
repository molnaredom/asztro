package controll.horoszkopok;

import controll.horoszkopEgysegek.Bolygo;
import controll.horoszkopEgysegek.Haz;

public class Fenyszog{


    public void beallitBolygonakHazat(Haz[] hazak, Bolygo[] bolygok) {
        //kiindulasi fokszam
        double ascfok = hazak[0].getFokszam();
        String ascjegye = hazak[0].getHazJegye().getJegyNev();
        for (int i = 1; i < 12; i++) {

            String aktjegy = hazak[i].getHazJegye().getJegyNev();


            hazak[i].setOsszFokszam(hanyadikjegyASCtol(ascjegye, aktjegy) * 30 - ascfok + hazak[i].getFokszam());
            //System.out.println( hazak[i].getHazszam()+" "+ascjegye+" "+aktjegy+" "+" "+ hanyadikjegyASCtol(ascjegye, aktjegy)+" "+hazak[i].getOsszFokszam());
        }

        for (int i = 0; i < 10; i++) {

            String aktjegy = bolygok[i].getJegy().getJegyNev();

            bolygok[i].setOsszFokszam(hanyadikjegyASCtol(ascjegye, aktjegy) * 30 - ascfok + bolygok[i].getFokszam());

        }
        for (int i = 0; i <10 ; i++) { //bolygo
            for (int j = 1; j <= 12; j++) {  //haz
                double bolyFok = bolygok[i].getOsszFokszam();
                if(j==12) {
                    if (bolyFok + 5 > 360) {
                        bolygok[i].setBolygoHazSzama(1);
                        break;
                    }
                    bolygok[i].setBolygoHazSzama(12);
                    break;
                }

                double hazFok = hazak[j].getOsszFokszam();
                if (hazak[j].getHaztipus().equals("sarok")){
                    if (bolyFok+5<hazFok) {
                        bolygok[i].setBolygoHazSzama(j);
                        break;
                    }
                } else {
                    if (bolyFok+3<hazFok) {
                        bolygok[i].setBolygoHazSzama(j);
                        break;
                    }
                }

            }

        }


    }

    private int hanyadikjegyASCtol(String kiindulasiJegy, String aktjegy) {
        int kiind = jegyetSzamra(kiindulasiJegy);
        int akt = jegyetSzamra(aktjegy);

        if (akt-kiind<1)akt+=12;

        return (akt-kiind);
    }

    /**
     * segedfuggveny bolygot vár aminek visszza adja a jegynevét
     */
    private String altjegynevU(Bolygo bolygo, String fenyszog, int melyik) {
        if (fenyszog.equals("konjukcio") && melyik == 0) return bolygo.getJegy().getJegyNev();
        else if (fenyszog.equals("konjukcio") && melyik == 1) return bolygo.getJegy().getMellette()[0];
        else if (fenyszog.equals("konjukcio") && melyik == 2) return bolygo.getJegy().getMellette()[1];

        else if (fenyszog.equals("oppozicio") && melyik == 0) return opposit(bolygo.getJegy().getJegyNev());
        else if (fenyszog.equals("oppozicio") && melyik == 1) return opposit(bolygo.getJegy().getMellette()[0]);
        else if (fenyszog.equals("oppozicio") && melyik == 2) return opposit(bolygo.getJegy().getMellette()[1]);
        else return null;

    }

    private String altjegynevB(Bolygo bolygo, String fenyszog, int melyik) {
        if (fenyszog.equals("kvadrat") && melyik == 0) return kvad(jegynev(bolygo))[0];
        else if (fenyszog.equals("kvadrat") && melyik == 1) return kvad(jegynev(bolygo))[1];
        else if (fenyszog.equals("kvadrat") && melyik == 2) return kvad(bolygo.getJegy().getMellette()[0])[0];
        else if (fenyszog.equals("kvadrat") && melyik == 3) return kvad(bolygo.getJegy().getMellette()[0])[1];
        else if (fenyszog.equals("kvadrat") && melyik == 4) return kvad(bolygo.getJegy().getMellette()[1])[0];
        else if (fenyszog.equals("kvadrat") && melyik == 5) return kvad(bolygo.getJegy().getMellette()[1])[1];

        else if (fenyszog.equals("trigon") && melyik == 0) return trig(jegynev(bolygo))[0];
        else if (fenyszog.equals("trigon") && melyik == 1) return trig(jegynev(bolygo))[1];
        else if (fenyszog.equals("trigon") && melyik == 2) return trig(bolygo.getJegy().getMellette()[0])[0];
        else if (fenyszog.equals("trigon") && melyik == 3) return trig(bolygo.getJegy().getMellette()[0])[1];
        else if (fenyszog.equals("trigon") && melyik == 4) return trig(bolygo.getJegy().getMellette()[1])[0];
        else if (fenyszog.equals("trigon") && melyik == 5) return trig(bolygo.getJegy().getMellette()[1])[1];

         /*else if (fenyszog.equals("szextil")&& melyik ==0) return szex( jegynev(bolygo))[0];
         else if (fenyszog.equals("szextil")&& melyik ==1) return szex( jegynev(bolygo))[1];
         else if (fenyszog.equals("szextil")&& melyik ==2) return szex(bolygo.getBolygoJegye().getMellette()[0])[0];
         else if (fenyszog.equals("szextil")&& melyik ==3) return szex(bolygo.getBolygoJegye().getMellette()[0])[1];
         else if (fenyszog.equals("szextil")&& melyik ==4) return szex(bolygo.getBolygoJegye().getMellette()[1])[0];
         else if (fenyszog.equals("szextil")&& melyik ==5) return szex(bolygo.getBolygoJegye().getMellette()[1])[1];
*/


        else return null;

    }

    private final String[][] fenyszogNevek = {{"konjukcio", "unaris"}, {"oppozicio", "unaris"}, {"kvadrat", "binaris"} };

    public void fenyszogKapcsLetrehozas(Bolygo[] bolygok) {
        for (Bolygo b : bolygok) {
            for (Bolygo keres : bolygok) {
                for (String[] nevek : fenyszogNevek) {
                    if (nevek[1].equals("unaris")) {
                        altFenyszogUnaris(b, keres, nevek[0]);
                    } else if (nevek[1].equals("binaris")) {
                        altFenyszogBinaris(b, keres, nevek[0]);
                    }

                }/*
                altFenyszogUnaris(b, keres, "oppozicio");
                altFenyszogBinaris(b, keres, "trigon");
                altFenyszogBinaris(b, keres, "szextil");*/

            }
        }
    }


    private void altFenyszogUnaris(Bolygo b, Bolygo keres, String fenyszogNev) {
        double bolygoFok = b.getFokszam();


        if (keres.getJegy().getJegyNev().equals(altjegynevU(b, fenyszogNev, 0)) &&
                Math.abs(bolygoFok - keres.getFokszam()) <= 10 &&
                keres != b //a ket bolyg nem ugyanaz
        ) {
            b.fenyszogKapcsHozzaad(fenyszogNev, keres.getNev());
        }

        //elottel levo jegy utolso 10 fokanak vizsgalata
        else if (keres.getJegy().getJegyNev().equals(altjegynevU(b, fenyszogNev, 1)) &&
                keres.getFokszam() >= 20 &&
                (30 - keres.getFokszam() + bolygoFok) <= 10
        ) {
            b.fenyszogKapcsHozzaad(fenyszogNev, keres.getNev());
        }

        //utana levo jegy elso 10 fokanak vizsgalata
        else if (keres.getJegy().getJegyNev().equals(altjegynevU(b, fenyszogNev, 2)) &&
                keres.getFokszam() <= 10 &&
                (keres.getFokszam() + 30 - bolygoFok) <= 10
        ) {
            b.fenyszogKapcsHozzaad(fenyszogNev, keres.getNev());
        }
    }

    private void altFenyszogBinaris(Bolygo b1, Bolygo b2, String fenyszogNev) {

        double bolygoFok = b1.getFokszam();

        //bal kvadrat
        if (jegynev(b1).equals(altjegynevB(b2, fenyszogNev, 0)) &&
                Math.abs(bolygoFok - b2.getFokszam()) <= 10 &&
                b2 != b1
        ) {
            b1.fenyszogKapcsHozzaad(fenyszogNev, b2.getNev());
        }

        //JOBB KVADRAT
        else if (jegynev(b1).equals(altjegynevB(b2, fenyszogNev, 1)) &&
                Math.abs(bolygoFok - b2.getFokszam()) <= 10 &&
                b2 != b1) {
            // System.out.println(kvad(jegynev(b2))[1]);
            b1.fenyszogKapcsHozzaad(fenyszogNev, b2.getNev());
        }

        //elottel levo jegy utolso 10 fokanak vizsgalata----bal kvadrat - balra jegy
        else if (jegynev(b1).equals(altjegynevB(b2, fenyszogNev, 2)) &&
                b2.getFokszam() >= 20 &&
                (30 - b2.getFokszam() + bolygoFok) <= 10 &&
                b2 != b1
        ) {
            b1.fenyszogKapcsHozzaad(fenyszogNev, b2.getNev());
        }

        //jobb kvadrat - balra jegy
        else if (jegynev(b1).equals(altjegynevB(b2, fenyszogNev, 3)) &&
                b2.getFokszam() >= 20 &&
                (30 - b2.getFokszam() + bolygoFok) <= 10 &&
                b2 != b1
        ) {
            b1.fenyszogKapcsHozzaad(fenyszogNev, b2.getNev());
        }

        //utana levo jegy elso 10 foka----bal kvadrat jobbra jegy
        else if (jegynev(b1).equals(altjegynevB(b2, fenyszogNev, 4)) &&
                b2.getFokszam() <= 10 &&
                (b2.getFokszam() + 30 - bolygoFok) <= 10 &&
                b2 != b1
        ) {
            b1.fenyszogKapcsHozzaad(fenyszogNev, b2.getNev());
        }

        //bal kvadrat jobbra jegy
        else if (jegynev(b1).equals(altjegynevB(b2, fenyszogNev, 5)) &&
                b2.getFokszam() <= 10 &&
                (b2.getFokszam() + 30 - bolygoFok) <= 10 &&
                b2 != b1
        ) {
            b1.fenyszogKapcsHozzaad(fenyszogNev, b2.getNev());
        }

    }


    private String jegynev(Bolygo bolygo) {
        return bolygo.getJegy().getJegyNev();
    }


    /**
     * a megfelelő jegyhez a megfelelő számot társítja
     */
    private String szamotJegyre(int szam) {
        //todo replace with hashmap
        return switch (szam) {
            case 1 -> "kos";
            case 2 -> "bika";
            case 3 -> "ikrek";
            case 4 -> "rak";
            case 5 -> "oroszlan";
            case 6 -> "szuz";
            case 7 -> "merleg";
            case 8 -> "skorpio";
            case 9 -> "nyilas";
            case 10 -> "bak";
            case 11 -> "vizonto";
            case 12 -> "halak";
            default -> "";
        };
    }

    /**
     * a megfelelő számhoz a megfelelő jegyet társítja
     */
    private int jegyetSzamra(String jegyNev) {
        return switch (jegyNev) {
            case "kos" -> 1;
            case "bika" -> 2;
            case "ikrek" -> 3;
            case "rak" -> 4;
            case "oroszlan" -> 5;
            case "szuz" -> 6;
            case "merleg" -> 7;
            case "skorpio" -> 8;
            case "nyilas" -> 9;
            case "bak" -> 10;
            case "vizonto" -> 11;
            case "halak" -> 12;
            default -> 0;
        };
    }


    /**
     * kisegítő fgv-ek
     */

    public String opposit(String atforditandoJegy) {
        return switch (atforditandoJegy) {
            case "kos" -> "merleg";
            case "bika" -> "skorpio";
            case "ikrek" -> "nyilas";
            case "rak" -> "bak";
            case "oroszlan" -> "vizonto";
            case "szuz" -> "halak";
            case "merleg" -> "kos";
            case "skorpio" -> "bika";
            case "nyilas" -> "ikrek";
            case "bak" -> "rak";
            case "vizonto" -> "oroszlan";
            case "halak" -> "szuz";
            default -> null;
        };
    }

    public String[] kvad(String atforditandoJegy) {
        int forditndojegySzama = jegyetSzamra(atforditandoJegy);

        return new String[]{
                szamotJegyre(((forditndojegySzama - 1 + 3 * 1) % 12) + 1), //a jegy utan következő első trigonális jegy
                szamotJegyre(((forditndojegySzama - 1 + 3 * 3) % 12) + 1)  //a jegy utan másodiknak következő trig jegy
        };
    }

    public String[] trig(String atforditandoJegy) {
        int forditndojegySzama = jegyetSzamra(atforditandoJegy);

        return new String[]{
                szamotJegyre(((forditndojegySzama - 1 + 4 * 1) % 12) + 1), //a jegy utan következő első trigonális jegy
                szamotJegyre(((forditndojegySzama - 1 + 4 * 2) % 12) + 1)  //a jegy utan másodiknak következő trig jegy
        };
    }
    //todo szextil bug - akkor is kiierja amikor nem kene, neha jo is de sokszor rosszul
    /*public String[] szex(String atforditandoJegy) {
        int forditndojegySzama = jegyetSzamra(atforditandoJegy);

        return new String[] {
                szamotJegyre(((forditndojegySzama-1 + 2*1)%12)+1), //a jegy utan következő első trigonális jegy
                szamotJegyre(((forditndojegySzama-1 + 2*5)%12)+1)  //a jegy utan másodiknak következő trig jegy
        };
    }*/



}
