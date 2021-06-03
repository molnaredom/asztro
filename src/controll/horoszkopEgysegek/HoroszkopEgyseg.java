package controll.horoszkopEgysegek;

public abstract class HoroszkopEgyseg {

    protected String nev;
    protected double fokszam;
    protected Jegy jegy;

    public HoroszkopEgyseg(String nev, Jegy jegy, double fokszam) {
        this.nev = nev;
        this.jegy = jegy;
        this.fokszam = fokszam;
    }

    /**
     * a megfelelő jegyhez a megfelelő számot társítja
     */
    protected String szamotJegyre(int szam) {
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
    protected int jegyetSzamra(String jegyNev) {
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




}
