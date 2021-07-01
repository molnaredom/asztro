package controll.elemzes.altalansoelemzes;

import controll.horoszkopEgysegek.Bolygo;
import modell.analogiak.egyszeresenOsszetettAnalogiak.bolygoJegyben.OsszesBolyoJegyben;

import javax.swing.plaf.synth.SynthOptionPaneUI;
import java.util.Arrays;

public interface BolygojegybenElemzes {


    static void bolygoJegybenElemzesKiirat(Bolygo[] bolygok) {

        int i = 0;
        for (String[][][] jegy : OsszesBolyoJegyben.Osszbolygo) { //bolygok
            try {
                System.out.println("\n---------------"+bolygok[i].getJegy().getJegyNev() +" "+bolygok[i].getNev()+"-----------------\n");
                for (String[] s : jegy[bolygok[i].getJegy().getJegySzama()-1]) {//jegy-analogia

                    Arrays.stream(s).forEach(System.out::println);
                }


            } catch (IndexOutOfBoundsException ie) {
                System.err.println(ie);
            } catch (Exception e) {
                System.err.println("egyebb ex");
            }
            i++;


        }

    }


}
