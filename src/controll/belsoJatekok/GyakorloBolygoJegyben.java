package controll.belsoJatekok;

import modell.analogiak.egyszeresenOsszetettAnalogiak.bolygoJegyben.OsszesBolyoJegyben;

import java.awt.datatransfer.Transferable;
import java.util.Random;
import java.util.Scanner;

public class GyakorloBolygoJegyben {

    OsszesBolyoJegyben oszb;
    Random random = new Random();
    Scanner sc = new Scanner(System.in);
    int pontszam=0;
    double kor = 0.0;

    public void play(){

            while (true){
                try {
                    int bolygo = random.nextInt(OsszesBolyoJegyben.osszbolygo.length);
                    int jegy = random.nextInt(12);
                    int analogiacsop =  random.nextInt(OsszesBolyoJegyben.osszbolygo[bolygo][jegy].length);
                    int analogia = random. nextInt(OsszesBolyoJegyben.osszbolygo[bolygo][jegy][analogiacsop].length);

                    System.out.println(OsszesBolyoJegyben.osszbolygo[bolygo][12][0][analogiacsop] +":");
                    System.out.println(OsszesBolyoJegyben.osszbolygo[bolygo][jegy][analogiacsop][analogia]);
                    System.out.println("írd be a tipped!");

                    String tipp = sc.nextLine();

                    String megoldas = szamotJegyre(jegy+1)+" "+OsszesBolyoJegyben.osszbolygo[bolygo][12][1][0];

                    kor++;
                    if (tipp.equals(megoldas)){
                        pontszam++;
                        System.out.println("Helyes megoldás");
                    }else{
                        System.out.print("Rossz megoldás\t");
                        System.out.print("Jó lett volna: \t");
                        System.out.println(megoldas);
                    }
                    System.out.println("az arányod jelenleg: "+ Math.round(100* pontszam/kor) +"%\n\n" );


                }catch (Exception e) {
                    //System.out.println(e);
                }
            }
        }



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


}
