package controll.jegyek;

import java.util.ArrayList;
import java.util.Arrays;


public class Jegy {
    private final String nev;
    private String elem;  //tuz viz fold levego
    private String minoseg;
    private String evszak;
    private boolean pozitiv;
    private float fokszam;
    private String opposit;
    //trigon kvadrat szeytil kbinkunksz  0. a jobb oldali 1. a bal oldali
    private String[] trigon;
    private String[] kvadrat;
    private String[] szextil;
    private String[] kvinkunksz;
    private int dekad; //1-3 kozti szam

    /** konstruktorok*/
    public Jegy(String nev) {
        this.nev = nev;
        setMinoseg();
        setElem();
        setEvszak();
        setPozitiv();
        setOpposit();
    }

    public Jegy(String nev, float fokszam) {
        this(nev);
        this.fokszam = fokszam;
    }


    /**setterek*/
    public void setTrigon() {
        switch (nev) {
            case "kos" : {
                this.trigon[0] = "oroszlan";
                this.trigon[1] = "nyilas";
            }
            case "bika" : {
                this.trigon[0] = "szuz";
                this.trigon[1] = "bak";
            }
            case "ikrek" : {
                this.trigon[0] = "merleg";
                this.trigon[1] = "vizonto";
            }
            case "rak" : {
                this.trigon[0] = "skorpio";
                this.trigon[1] = "halak";
            }
            case "oroszlan" : {
                this.trigon[0] = "nyilas";
                this.trigon[1] = "kos";
            }
            case "szuz" : {
                this.trigon[0] = "bak";
                this.trigon[1] = "bika";
            }
            case "merleg" : {
                this.trigon[0] = "vizonto";
                this.trigon[1] = "ikrek";
            }
            case "skorpio" : {
                this.trigon[0] = "halak";
                this.trigon[1] = "rak";
            }
            case "nyilas" : {
                this.trigon[0] = "kos";
                this.trigon[1] = "oroszlan";
            }
            case "bak" : {
                this.trigon[0] = "bika";
                this.trigon[1] = "szuz";
            }
            case "vizonto" : {
                this.trigon[0] = "ikrek";
                this.trigon[1] = "merleg";
            }
            case "halak" : {
                this.trigon[0] = "rak";
                this.trigon[1] = "skorpio";
            }
        }
    }

    public void setKvadrat() {
        switch (nev) {
            case "kos" : {
                this.trigon[0] = "rak";
                this.trigon[1] = "bak";
            }
            case "bika" : {
                this.trigon[0] = "oroszlan";
                this.trigon[1] = "vizonto";
            }
            case "ikrek" : {
                this.trigon[0] = "szuz";
                this.trigon[1] = "halak";
            }
            case "rak" : {
                this.trigon[0] = "merleg";
                this.trigon[1] = "kos";
            }
            case "oroszlan" : {
                this.trigon[0] = "skorpio";
                this.trigon[1] = "bika";
            }
            case "szuz" : {
                this.trigon[0] = "nyilas";
                this.trigon[1] = "ikrek";
            }
            case "merleg" : {
                this.trigon[0] = "bak";
                this.trigon[1] = "rak";
            }
            case "skorpio" : {
                this.trigon[0] = "vizonto";
                this.trigon[1] = "oroszlan";
            }
            case "nyilas" : {
                this.trigon[0] = "halak";
                this.trigon[1] = "szuz";
            }
            case "bak" : {
                this.trigon[0] = "kos";
                this.trigon[1] = "merleg";
            }
            case "vizonto" : {
                this.trigon[0] = "bika";
                this.trigon[1] = "skorpio";
            }
            case "halak" : {
                this.trigon[0] = "ikrek";
                this.trigon[1] = "nyilas";
            }
        }
    }

    public void setSzextil(String[] szextil) {
        this.szextil = szextil;
    }

    public void setKvinkunksz(String[] kvinkunksz) {
        this.kvinkunksz = kvinkunksz;
    }

    public void setDekad() {
        if (fokszam<0 || fokszam>30)
            System.err.println("fok rosszul van megadva max 30 min 0");
        else if (fokszam<10){
            this.dekad = 1;
        }else  if (fokszam<20){
            this.dekad = 2;
        } else if (fokszam<30){
            this.dekad =3;
        }
    }

    public void setMinoseg() {

        ArrayList<String> kardinalis = new ArrayList<>(Arrays.asList("kos","rak","merleg","bak"));
        ArrayList<String> szilard = new ArrayList<>(Arrays.asList("bika","oroszlan","skorpio","vizonto"));
        ArrayList<String> valtozo = new ArrayList<>(Arrays.asList("ikrek","szuz","nyilas","halak"));


        if (kardinalis.contains(nev)){
            this.minoseg = "kardinalis";
        }  else if (szilard.contains(nev)) {
            this.minoseg = "szilard";
        }  else if (valtozo.contains(nev)) {
            this.minoseg = "valtozo";
        } else {
            System.out.println("hibas jegymegadas setminoseg  "+nev);
            this.minoseg = "";
        }

    }

    private void setOpposit() {
        switch (nev) {
            case "kos" -> this.opposit = "merleg";
            case "bika" -> this.opposit = "skorpio";
            case "ikrek" -> this.opposit = "nyilas";
            case "rak" -> this.opposit = "bak";
            case "oroszlan" -> this.opposit = "vizonto";
            case "szuz" -> this.opposit = "halak";
            case "merleg" -> this.opposit = "kos";
            case "skorpio" -> this.opposit = "bika";
            case "nyilas" -> this.opposit = "ikrek";
            case "bak" -> this.opposit = "rak";
            case "vizonto" -> this.opposit = "oroszlan";
            case "halak" -> this.opposit = "szuz";
        }


    }

    private void setElem() {

        ArrayList<String> tuz = new ArrayList<>(Arrays.asList("kos","oroszlan","nyilas"));
        ArrayList<String> fold = new ArrayList<>(Arrays.asList("bika","szuz","bak"));
        ArrayList<String> levego = new ArrayList<>(Arrays.asList("ikrek","merleg","vizonto"));
        ArrayList<String> viz = new ArrayList<>(Arrays.asList("rak","skorpio","halak"));

        if (tuz.contains(nev)){
            this.elem = "tuz";
        }  else if (fold.contains(nev)) {
            this.elem = "fold";
        }  else if (levego.contains(nev)) {
            this.elem = "levego";
        } else if (viz.contains(nev)) {
            this.elem = "viz";
        } else {
            System.out.println("hibas jegymegadas setminoseg  "+nev);
            this.elem = "";
        }
    }

    private void setEvszak() {
        ArrayList<String> tavasz = new ArrayList<>(Arrays.asList("kos","bika","ikrek"));
        ArrayList<String> nyar = new ArrayList<>(Arrays.asList("rak","oroszlan","szuz"));
        ArrayList<String> osz = new ArrayList<>(Arrays.asList("merleg","skorpio","nyilas"));
        ArrayList<String> tel = new ArrayList<>(Arrays.asList("bak","vizonto","halak"));

        if (tavasz.contains(nev)){
            this.evszak = "tavasz";
        }  else if (nyar.contains(nev)) {
            this.evszak = "nyar";
        }  else if (osz.contains(nev)) {
            this.evszak = "osz";
        } else if (tel.contains(nev)) {
            this.evszak = "tel";
        } else {
            System.err.println("hibas jegymegadas setevszak");
            this.evszak= "";
        }

    }

    private void setPozitiv() {
        ArrayList<String> poz = new ArrayList<>(Arrays.asList("kos","ikrek","oroszlan","merleg","nyilas","vizonto"));
        ArrayList<String> neg = new ArrayList<>(Arrays.asList("bika","rak","szuz","skorpio","bak","halak"));

        if (poz.contains(nev.toLowerCase())){
            this.pozitiv = true;
        }  else if (neg.contains(nev.toLowerCase())) {
            this.pozitiv = false;
        }else {
            System.out.println("hibas jegymegadas setpozitiv  "+nev);
            this.pozitiv = true;
        }

    }




    /**getterek*/
    public String getOpposit() {
        return opposit;
    }

    public String[] getKvinkunksz() {
        return kvinkunksz;
    }

    public String[] getKvadrat() {
        return kvadrat;
    }

    public String[] getSzextil() {
        return szextil;
    }

    public String getMinoseg() {
        return minoseg;
    }

    public String[] getTrigon() {
        return trigon;
    }

    public String getNev() {
        return nev;
    }


    public String getElem() {
        return elem;
    }

    public String getEvszak() {
        return evszak;
    }

    public boolean isPozitiv() {
        return pozitiv;
    }

    public float getFokszam() {
        return fokszam;
    }

    public int getDekad() {
        return dekad;
    }
}

