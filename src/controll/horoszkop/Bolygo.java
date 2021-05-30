package controll.horoszkop;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


public class Bolygo {
    private final String nev;
    private String szint;
    private int pont;
    private double fokszam;

    private final Jegy bolygoJegye;
    private Haz bolygoHaza;
    private String dekadJegy;
    private int dekadSzam;
    //string 0 eleme a fenyszog neve , 1 eleme a bolygo amivel kapcsolatban áll
    private List<String[]> fenyszogKapcsoaltok = new ArrayList<>();



    /** konstruktorok*/
    public Bolygo(String nev, Jegy bolygoJegye) {
        this.nev = nev;
        setPont();
        setSzint();
        this.bolygoJegye = bolygoJegye;
    }

    public Bolygo(String nev, Jegy bolygoJegye, Haz bolygoHaza, double fokszam) {
        this(nev, bolygoJegye);
        this.fokszam = fokszam;
        this.bolygoHaza = bolygoHaza;
        setDekadSzam();
        setDekadJegy();

    }

    public void fenyszogKapcsHozzaad(String fenyszog, String bolygo) {
        fenyszogKapcsoaltok.add(new String[] {fenyszog,bolygo});
    }

    public void setFenyszogKapcsoaltok(List<String[]> fenyszogKapcsoaltok) {
        this.fenyszogKapcsoaltok = new ArrayList<>();
    }



    public List<String[]> getFenyszogKapcsoaltok() {
        return fenyszogKapcsoaltok;
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
        dekadJegy = bolygoJegye.getDekadJegyek()[dekadSzam-1];
    }


    /**getterek*/

    public Jegy getBolygoJegye() {
        return bolygoJegye;
    }
    public double getFokszam() {
        return fokszam;
    }
    public Haz getBolygoHaza() {
        return bolygoHaza;
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


}
