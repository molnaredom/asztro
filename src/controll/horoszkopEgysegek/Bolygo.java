package controll.horoszkopEgysegek;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class Bolygo extends HoroszkopEgyseg {
    private String szint;
    private int pont;
    private int bolygoHazSzama;
    private String dekadJegy;
    private int dekadSzam;
    private double osszFokszam;

    //string 0 eleme a fenyszog neve , 1 eleme a bolygo amivel kapcsolatban áll
    private List<String[]> fenyszogKapcsoaltok = new ArrayList<>();


    /** konstruktor*/
    public Bolygo(String nev, Jegy bolygoJegye, double fokszam) {
        super(nev,bolygoJegye,fokszam);
        setPont();
        setSzint();
        setDekadSzam();
        setDekadJegy();
    }

    /** műveletek */
    public void fenyszogKapcsHozzaad(String fenyszog, String bolygo) {
        fenyszogKapcsoaltok.add(new String[] {fenyszog,bolygo});
    }


    /**setterek*/

    public void setDekadSzam() {
        if (0.0<=fokszam && 10.0>fokszam) {
            this.dekadSzam =1;
        } else if (10.0<=fokszam && 20.0>fokszam) {
            this.dekadSzam =2;
        }else if (20.0<=fokszam && 30.0>fokszam) {
            this.dekadSzam =3;
        }
    }

    private void setSzint() {

        //pluto? neptun?

        ArrayList<String> also = new ArrayList<>(Arrays.asList("mars","venusz"));
        ArrayList<String> kozepso = new ArrayList<>(Arrays.asList("hold","jupiter","merkur","neptun","pluto"));
        ArrayList<String> felso = new ArrayList<>(Arrays.asList("szaturnusz","nap","uranusz"));


        if (also.contains(nev)){
            this.szint = "also";
        }  else if (kozepso.contains(nev)) {
            this.szint = "kozepso";
        }  else if (felso.contains(nev)) {
            this.szint = "felso";
        } else {
            System.err.println("hibas jegymegadas:"+nev );
            this.szint = "";
        }
    }

    public void setPont() {

        ArrayList<String> ketpont = new ArrayList<>(Arrays.asList("nap", "hold", "merkur"));
        ArrayList<String> egypont = new ArrayList<>(Arrays.asList("jupiter","neptun","pluto","mars","venusz","szaturnusz","uranusz"));

        if (ketpont.contains(nev)){
            this.pont = 2;
        }  else if (egypont.contains(nev)) {
            this.pont = 1;
        } else {
            System.err.println("hibas setPont:"+nev );
            this.pont = 0;
        }
    }

    public void setDekadJegy() {
        dekadJegy = jegy.getDekadJegyek()[dekadSzam-1];
    }

    public void setOsszFokszam(double osszFokszam) {
        this.osszFokszam = osszFokszam;
    }

    public void setBolygoHazSzama(int hazszam) {
        bolygoHazSzama= hazszam;
    }

    /**getterek*/

    public Jegy getJegy() {
        return jegy;
    }
    public double getFokszam() {
        return fokszam;
    }
    public int getBolygoHazSzama() {
        return bolygoHazSzama;
    }
    public String getSzint() {
        return szint;
    }
    public String getNev() {
        return nev;
    }
    public int getPont() {
        return pont;
    }
    public int getDekadSzam() {
        return dekadSzam;
    }
    public String getDekadJegy() {
        return dekadJegy;
    }
    public List<String[]> getFenyszogKapcsoaltok() {
        return fenyszogKapcsoaltok;
    }
    public double getOsszFokszam() {
        return osszFokszam;
    }
}
