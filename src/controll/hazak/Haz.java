package controll.hazak;

import controll.bolygok.Bolygo;
import controll.jegyek.Jegy;

public class Haz {

    private int hazszam;
    private String[] analogiai;
    private String haztipus;

    private Jegy jegyHazban;
    private Bolygo hazraHatoBolygo;
    private Bolygo[] hazraHatoBolygok;


    public Haz(int hazszam) {
        setHazszam(hazszam);
    }

    public Haz(int hazszam, Jegy jegyHazban) {
        this(hazszam);
        this.jegyHazban = jegyHazban;
    }

    public Haz(int hazszam, Jegy jegyHazban, Bolygo hazraHatoBolygo) {
        this(hazszam);
        this.jegyHazban = jegyHazban;
        this.hazraHatoBolygo = hazraHatoBolygo;
    }

    public Haz(int hazszam, Jegy jegyHazban, Bolygo[] hazraHatoBolygok) {
        this(hazszam);
        this.jegyHazban = jegyHazban;
        this.hazraHatoBolygok = hazraHatoBolygok;
    }


    public String hazUra() {
        if (jegyHazban.getNev().equals("kos") || jegyHazban.getNev().equals("skorpio")) {
            return "mars";
        } else if (jegyHazban.getNev().equals("bika") || jegyHazban.getNev().equals("merleg")) {
            return "venusz";
        } else if (jegyHazban.getNev().equals("ikrek") || jegyHazban.getNev().equals("szuz")) {
            return "merkur";
        } else if (jegyHazban.getNev().equals("nyilas") || jegyHazban.getNev().equals("halak")) {
            return "jupiter";
        } else if (jegyHazban.getNev().equals("bak") || jegyHazban.getNev().equals("vizonto")) {
            return "szaturnusz";
        } else if (jegyHazban.getNev().equals("oroszlan")) {
            return "nap";
        } else if (jegyHazban.getNev().equals("rak")) {
            return "hold";
        } else {
            System.err.println("nincs hazura problem");
            return "";
        }
    }


    public int getHazszam() {
        return hazszam;
    }

    private void setHazszam(int hazszam) {
        if (hazszam > 12 || hazszam < 1) {
            this.hazszam = 1;
            System.err.println("rosszul lett beallitva a haz");
        } else this.hazszam = hazszam;
    }

    public String[] getAnalogiai() {
        return analogiai;
    }

    public String getHaztipus() {
        return haztipus;
    }

    public Jegy getJegyHazban() {
        return jegyHazban;
    }

    public Bolygo getHazraHatoBolygo() {
        return hazraHatoBolygo;
    }

    public Bolygo[] getHazraHatoBolygok() {
        return hazraHatoBolygok;
    }

}