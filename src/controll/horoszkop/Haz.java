package controll.horoszkop;

public class Haz {

    private int hazszam;
    private String[] analogiai;
    private String haztipus;

    private Jegy hazJegye;
    private Bolygo hazraHatoBolygo;
    private Bolygo[] hazraHatoBolygok;


    public Haz(int hazszam) {
        setHazszam(hazszam);
    }

    public Haz(int hazszam, Jegy jegyHazban) {
        this(hazszam);
        this.hazJegye = jegyHazban;
    }

    public Haz(int hazszam, Jegy jegyHazban, Bolygo hazraHatoBolygo) {
        this(hazszam);
        this.hazJegye = jegyHazban;
        this.hazraHatoBolygo = hazraHatoBolygo;
    }

    public Haz(int hazszam, Jegy jegyHazban, Bolygo[] hazraHatoBolygok) {
        this(hazszam);
        this.hazJegye = jegyHazban;
        this.hazraHatoBolygok = hazraHatoBolygok;
    }


    public String hazUralkodoBolygoja() {
        if (hazJegye.getNev().equals("kos") || hazJegye.getNev().equals("skorpio")) {
            return "mars";
        } else if (hazJegye.getNev().equals("bika") || hazJegye.getNev().equals("merleg")) {
            return "venusz";
        } else if (hazJegye.getNev().equals("ikrek") || hazJegye.getNev().equals("szuz")) {
            return "merkur";
        } else if (hazJegye.getNev().equals("nyilas") || hazJegye.getNev().equals("halak")) {
            return "jupiter";
        } else if (hazJegye.getNev().equals("bak") || hazJegye.getNev().equals("vizonto")) {
            return "szaturnusz";
        } else if (hazJegye.getNev().equals("oroszlan")) {
            return "nap";
        } else if (hazJegye.getNev().equals("rak")) {
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

    public Jegy getHazJegye() {
        return hazJegye;
    }

    public Bolygo getHazraHatoBolygo() {
        return hazraHatoBolygo;
    }

    public Bolygo[] getHazraHatoBolygok() {
        return hazraHatoBolygok;
    }

}