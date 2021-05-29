package controll.horoszkopok;

import controll.horoszkop.Bolygo;
import controll.horoszkop.Haz;

public abstract class Horoszkop {

    /**controll.bolygok*/
    boolean ferfi;
    Bolygo nap;
    Bolygo hold;
    Bolygo merkur;
    Bolygo mars;
    Bolygo venusz;
    Bolygo jupiter;
    Bolygo szaturnusz;
    Bolygo uranusz;
    Bolygo neptun;
    Bolygo pluto;

    Bolygo[] bolygok;

    /**controll.hazak*/

    Haz egyes;
    Haz kettes;
    Haz harmas;
    Haz negyes;
    Haz otos;
    Haz hatos;
    Haz hetes;
    Haz nyolcas;
    Haz kilences;
    Haz tizes;
    Haz tizenegyes;
    Haz tizenkettes;

    Haz[] hazak;


    public Horoszkop(boolean ferfi,Bolygo nap, Bolygo hold, Bolygo merkur, Bolygo mars, Bolygo venusz, Bolygo jupiter, Bolygo szaturnusz, Bolygo uranusz, Bolygo neptun, Bolygo pluto, Haz egyes, Haz kettes, Haz harmas, Haz negyes, Haz otos, Haz hatos, Haz hetes, Haz nyolcas, Haz kilences, Haz tizes, Haz tizenegyes, Haz tizenkettes) {
        this.ferfi =ferfi;
        this.nap = nap;
        this.hold = hold;
        this.merkur = merkur;
        this.mars = mars;
        this.venusz = venusz;
        this.jupiter = jupiter;
        this.szaturnusz = szaturnusz;
        this.uranusz = uranusz;
        this.neptun = neptun;
        this.pluto = pluto;
        setBolygok();
        this.egyes = egyes;
        this.kettes = kettes;
        this.harmas = harmas;
        this.negyes = negyes;
        this.otos = otos;
        this.hatos = hatos;
        this.hetes = hetes;
        this.nyolcas = nyolcas;
        this.kilences = kilences;
        this.tizes = tizes;
        this.tizenegyes = tizenegyes;
        this.tizenkettes = tizenkettes;
        setHazak();
    }

    //protected abstract Haz[] setHazak(Haz egyes, Haz kettes, Haz harmas, Haz negyes, Haz otos, Haz hatos, Haz hetes, Haz nyolcas, Haz kilences, Haz tizes, Haz tizenegyes, Haz tizenkettes);

    public void setBolygok() {
        this.bolygok = new Bolygo[]{nap, hold, merkur, mars, venusz, jupiter, szaturnusz, uranusz, neptun, pluto};;
    }

    public abstract void elemzes();

    public void setHazak() {

        this.hazak = new Haz[]{egyes, kettes, harmas, negyes, otos, hatos, hetes, nyolcas, kilences, tizes, tizenegyes, tizenkettes};
    }
}
