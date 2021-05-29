package controll.horoszkop;

import java.util.ArrayList;
import java.util.Arrays;


public class Bolygo {
    private final String nev;
    private String szint;
    private int pont;
    private double fokszam;

    private Jegy BolygoJegye;
    private Haz BolygoHaza;

    public int getPont() {
        return pont;
    }

    /** konstruktorok*/
    public Bolygo(String nev, Jegy bolygoJegye) {
        this.nev = nev;
        setPont();
        setSzint();
        BolygoJegye = bolygoJegye;
    }

    public Bolygo(String nev, Jegy bolygoJegye, Haz bolygoHaza) {
        this(nev, bolygoJegye);
        BolygoHaza = bolygoHaza;
    }

    public Bolygo(String nev, Jegy bolygoJegye, Haz bolygoHaza,double fokszam) {
        this(nev, bolygoJegye);
        BolygoHaza = bolygoHaza;
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

    public Jegy getBolygoJegye() {
        return BolygoJegye;
    }

    public Haz getBolygoHaza() {
        return BolygoHaza;
    }
    public String getSzint() {
        return szint;
    }
    public String getNev() {
        return nev;
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
}
