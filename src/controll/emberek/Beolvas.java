package controll.emberek;

import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Beolvas {



    public static List<String[]> beolv(String nev) {

        List<String[]> adatLista = new ArrayList<>();

        File text = new File("src/controll/emberek/adatok.txt");
        try {
            Scanner sc = new Scanner(text);
            while (sc.hasNextLine()) {
                if ((sc.nextLine()).startsWith("*" + nev)) {
                    while (sc.hasNextLine()) {
                        String sor = sc.nextLine();
                        if (sor.startsWith("*")) return adatLista;
                        adatLista.add(sor.split(";"));
                    }
                }
            }
        } catch (Exception e) {
            System.err.println(e);
        }
        return adatLista;

    }


}
