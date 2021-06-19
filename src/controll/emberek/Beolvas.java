package controll.emberek;


import java.io.File;
import java.util.Scanner;

public class Beolvas {

public static void beolv()  {
    File text = new File("src/controll/emberek/adatok.txt");
    try {
        Scanner sc = new Scanner(text);
        while(sc.hasNextLine()){
            String line = sc.nextLine();
            System.out.println(line);
        }
    } catch (Exception e) {
        System.err.println(e);
    }



}


}
