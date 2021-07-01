package controll.horoszkopEgysegek;

import java.util.*;


public class Jegy {
    private final String jegyNev;
    /**
     * a jegynek megfelelo szam
     */
    private int jegySzama;
    private String elem;  //tuz viz fold levego
    private String minoseg;
    private String evszak;
    private boolean pozitiv;
    private String opposit;
    private final String[] mellette = new String[2]; // 2 mellette lévő jegy neve
    //trigon kvadrat szeytil kbinkunksz  0. a jobb oldali 1. a bal oldali
    private final String[] dekadJegyek = new String[3];
    private String[] kvadrat;
    private String[] szextil;
    private String[] kvinkunksz;
    Map<Integer,String> jegyekMap = new HashMap<>();


    private void setJegySzama() {
        switch (jegyNev) {
            case "kos" -> this.jegySzama = 1;
            case "bika" -> this.jegySzama = 2;
            case "ikrek" -> this.jegySzama = 3;
            case "rak" -> this.jegySzama = 4;
            case "oroszlan" -> this.jegySzama = 5;
            case "szuz" -> this.jegySzama = 6;
            case "merleg" -> this.jegySzama = 7;
            case "skorpio" -> this.jegySzama = 8;
            case "nyilas" -> this.jegySzama = 9;
            case "bak" -> this.jegySzama = 10;
            case "vizonto" -> this.jegySzama =11;
            case "halak" -> this.jegySzama = 12;
        }
    }

    private void setJegyekMap() {

        jegyekMap.put(1,"kos");
        jegyekMap.put(2,"bika");
        jegyekMap.put(3,"ikrek");
        jegyekMap.put(4,"rak");
        jegyekMap.put(5,"oroszlan");
        jegyekMap.put(6,"szuz");
        jegyekMap.put(7,"merleg");
        jegyekMap.put(8,"skorpio");
        jegyekMap.put(9,"nyilas");
        jegyekMap.put(10,"bak");
        jegyekMap.put(11,"vizonto");
        jegyekMap.put(12,"halak");
    }

    public void setMellette() {
        //jobbra levő a 0. elem , balra levo az 1. elem pl ha kos akkor halak a 0. és bika  az 1.
        if (jegySzama!= 1)mellette[0] = jegyekMap.get(jegySzama-1);
        else mellette[0]= "halak";

        if (jegySzama!=12)mellette[1] = jegyekMap.get(jegySzama+1);
        else mellette[1] = "kos";

    }

    /** konstruktorok*/
    public Jegy(String nev) {
        this.jegyNev = nev;
        setJegySzama();
        setJegyekMap();
        setMinoseg();
        setElem();
        setEvszak();
        setPozitiv();
        setOpposit();
        dekadSzerintrendezes();
        setMellette();
    }



    /**setterek*/
    private void dekadSzerintrendezes() {
        int maradek =(jegySzama-1)%4;//0-11
        int eltolas = (jegySzama-1)/4; //ennyivel lesz eltolva BALRA pl 1 tolas {4,8,12}--> {8,12,4}
        List<Integer> eredmeny = new ArrayList<>();
        System.out.println();

        /**azokat a szamokat teszi bele a listaba amelyek megfelelo maradekuak, vagyis trigonalisan megfelelo jegyben vannak
        //de ez minden esetben pl 0-3 mal kezdődik pl 3 7 11 nincs kiigazitva*/
        for (int i = 0; i <= 11; i++) {
            if ( (i%4)==maradek) {
                eredmeny.add(i);
            }
        }

        /**sorrend koorigalas
        //ahanyszor iteral annyiszor eltoljuk balra a tombot 1 el pl 0 4 8 bol 4 8 0 legyen
        ezzel ki lesz igazitva es ehhez képest lehet nezni dekadnak megfeleloan hanyat lepjunk*/
        for (int i = 0; i < eltolas; i++) {
            eredmeny.add(0,eredmeny.get(2));//2.indexu elemet az elejere szurjuk
            eredmeny.add(0,eredmeny.get(1+1));//eredeti1. indexu elemet az elejere szurjuk

            eredmeny.remove(3);//az utolso ket elemet kitoroljuk nem alljon feleslegesen
            eredmeny.remove(3);
        }


        /**
         * String tömbbe rendezi a jegyeket már igazított formában pl 0 4 8 -> 1 5 9 -> kos oroszlan nyilas*/
        dekadJegyek[0] = jegyekMap.get(eredmeny.get(0)+1);//Map(List(szam))
        dekadJegyek[1] = jegyekMap.get(eredmeny.get(1)+1);
        dekadJegyek[2] = jegyekMap.get(eredmeny.get(2)+1);

    }

    private void setKvadrat() {
        //todo moduloval megcsinalni + ne a drakadot valtoztassa
        switch (jegyNev) {
            case "kos" : {
                this.dekadJegyek[0] = "rak";
                this.dekadJegyek[1] = "bak";
            }
            case "bika" : {
                this.dekadJegyek[0] = "oroszlan";
                this.dekadJegyek[1] = "vizonto";
            }
            case "ikrek" : {
                this.dekadJegyek[0] = "szuz";
                this.dekadJegyek[1] = "halak";
            }
            case "rak" : {
                this.dekadJegyek[0] = "merleg";
                this.dekadJegyek[1] = "kos";
            }
            case "oroszlan" : {
                this.dekadJegyek[0] = "skorpio";
                this.dekadJegyek[1] = "bika";
            }
            case "szuz" : {
                this.dekadJegyek[0] = "nyilas";
                this.dekadJegyek[1] = "ikrek";
            }
            case "merleg" : {
                this.dekadJegyek[0] = "bak";
                this.dekadJegyek[1] = "rak";
            }
            case "skorpio" : {
                this.dekadJegyek[0] = "vizonto";
                this.dekadJegyek[1] = "oroszlan";
            }
            case "nyilas" : {
                this.dekadJegyek[0] = "halak";
                this.dekadJegyek[1] = "szuz";
            }
            case "bak" : {
                this.dekadJegyek[0] = "kos";
                this.dekadJegyek[1] = "merleg";
            }
            case "vizonto" : {
                this.dekadJegyek[0] = "bika";
                this.dekadJegyek[1] = "skorpio";
            }
            case "halak" : {
                this.dekadJegyek[0] = "ikrek";
                this.dekadJegyek[1] = "nyilas";
            }
        }
    }

    public void setSzextil(String[] szextil) {
        this.szextil = szextil;
    }

    public void setKvinkunksz(String[] kvinkunksz) {
        this.kvinkunksz = kvinkunksz;
    }


    public void setMinoseg() {

        ArrayList<String> kardinalis = new ArrayList<>(Arrays.asList("kos","rak","merleg","bak"));
        ArrayList<String> szilard = new ArrayList<>(Arrays.asList("bika","oroszlan","skorpio","vizonto"));
        ArrayList<String> valtozo = new ArrayList<>(Arrays.asList("ikrek","szuz","nyilas","halak"));


        if (kardinalis.contains(jegyNev)){
            this.minoseg = "kardinalis";
        }  else if (szilard.contains(jegyNev)) {
            this.minoseg = "szilard";
        }  else if (valtozo.contains(jegyNev)) {
            this.minoseg = "valtozo";
        } else {
            System.out.println("hibas jegymegadas setminoseg  "+ jegyNev);
            this.minoseg = "";
        }

    }

    private void setOpposit() {
        switch (jegyNev) {
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

        if (tuz.contains(jegyNev)){
            this.elem = "tuz";
        }  else if (fold.contains(jegyNev)) {
            this.elem = "fold";
        }  else if (levego.contains(jegyNev)) {
            this.elem = "levego";
        } else if (viz.contains(jegyNev)) {
            this.elem = "viz";
        } else {
            System.out.println("hibas jegymegadas setminoseg  "+ jegyNev);
            this.elem = "";
        }
    }

    private void setEvszak() {
        ArrayList<String> tavasz = new ArrayList<>(Arrays.asList("kos","bika","ikrek"));
        ArrayList<String> nyar = new ArrayList<>(Arrays.asList("rak","oroszlan","szuz"));
        ArrayList<String> osz = new ArrayList<>(Arrays.asList("merleg","skorpio","nyilas"));
        ArrayList<String> tel = new ArrayList<>(Arrays.asList("bak","vizonto","halak"));

        if (tavasz.contains(jegyNev)){
            this.evszak = "tavasz";
        }  else if (nyar.contains(jegyNev)) {
            this.evszak = "nyar";
        }  else if (osz.contains(jegyNev)) {
            this.evszak = "osz";
        } else if (tel.contains(jegyNev)) {
            this.evszak = "tel";
        } else {
            System.err.println("hibas jegymegadas setevszak");
            this.evszak= "";
        }

    }

    private void setPozitiv() {
        ArrayList<String> poz = new ArrayList<>(Arrays.asList("kos","ikrek","oroszlan","merleg","nyilas","vizonto"));
        ArrayList<String> neg = new ArrayList<>(Arrays.asList("bika","rak","szuz","skorpio","bak","halak"));

        if (poz.contains(jegyNev.toLowerCase())){
            this.pozitiv = true;
        }  else if (neg.contains(jegyNev.toLowerCase())) {
            this.pozitiv = false;
        }else {
            System.out.println("hibas jegymegadas setpozitiv  "+ jegyNev);
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

    public String[] getDekadJegyek() {
        return dekadJegyek;
    }

    public String getJegyNev() {
        return jegyNev;
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

    public String[] getMellette() {
        return mellette;
    }

    public int getJegySzama() {
        return jegySzama;
    }
}

