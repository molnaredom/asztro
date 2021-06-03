package controll.horoszkopEgysegek;

public class Haz extends HoroszkopEgyseg {

    private int hazszamNUM;

    private String haztipus;

    private final Jegy hazJegye;

    private double osszFokszam;

    private final double fokszam;

    public Haz(String hazszamSTR, Jegy jegyHazban, double fokszam) {
        super(hazszamSTR,jegyHazban,fokszam);

        setHazszamNUM( Integer.parseInt(hazszamSTR));
        this.hazJegye = jegyHazban;
        this.fokszam = fokszam;
        setHaztipus();
    }
    public String getHaztipus() {
        return haztipus;
    }

    private void setHaztipus() {
        if ((hazszamNUM%3)==1) haztipus="sarok";
        if ((hazszamNUM%3)==2) haztipus="koveto";
        if ((hazszamNUM%3)==0) haztipus="hanyatlo";

    }

    public double getOsszFokszam() {
        return osszFokszam;
    }

    public void setOsszFokszam(double osszFokszam) {
        this.osszFokszam = osszFokszam;
    }



    public double getFokszam() {
        return fokszam;
    }

    public String hazUralkodoBolygoja() {
        switch (hazJegye.getJegyNev()) {
            case "kos":
            case "skorpio":
                return "mars";
            case "bika":
            case "merleg":
                return "venusz";
            case "ikrek":
            case "szuz":
                return "merkur";
            case "nyilas":
            case "halak":
                return "jupiter";
            case "bak":
            case "vizonto":
                return "szaturnusz";
            case "oroszlan":
                return "nap";
            case "rak":
                return "hold";
            default:
                System.err.println("nincs hazura problem");
                return "";
        }
    }


    public int getHazszam() {
        return hazszamNUM;
    }

    private void setHazszamNUM(int hazszam) {
        if (hazszam > 12 || hazszam < 1) {
            this.hazszamNUM = 1;
            System.err.println("rosszul lett beallitva a hazszam : "+hazszam);
        } else this.hazszamNUM = hazszam;
    }

    public Jegy getHazJegye() {
        return hazJegye;
    }

}