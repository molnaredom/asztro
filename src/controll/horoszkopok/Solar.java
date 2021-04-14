package controll.horoszkopok;

import controll.bolygok.Bolygo;
import controll.hazak.Haz;

public class Solar extends Horoszkop{

    public Solar(boolean ferfi,Bolygo nap, Bolygo hold, Bolygo merkur, Bolygo mars, Bolygo venusz, Bolygo jupiter, Bolygo szaturnusz, Bolygo uranusz, Bolygo neptun, Bolygo pluto, Haz egyes, Haz kettes, Haz harmas, Haz negyes, Haz otos, Haz hatos, Haz hetes, Haz nyolcas, Haz kilences, Haz tizes, Haz tizenegyes, Haz tizenkettes) {
        super(ferfi ,nap, hold, merkur, mars, venusz, jupiter, szaturnusz, uranusz, neptun, pluto, egyes, kettes, harmas, negyes, otos, hatos, hetes, nyolcas, kilences, tizes, tizenegyes, tizenkettes);
    }

    @Override
    public void elemzes() {

    }
}
