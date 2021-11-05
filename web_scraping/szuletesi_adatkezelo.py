def get_szuletesi_adat_nev_alapjan(keresett_nev):
    try:
        with open("../kepletek/szuletesi_adatok.csv") as keplet_adattomb:
            for sor_adat in keplet_adattomb:

                if sor_adat.split(";")[0] == keresett_nev:
                    horoszkop_adat_tomb = sor_adat.split(";")
                    return {
                        "nev": horoszkop_adat_tomb[0],
                        "horoszkoptipus": horoszkop_adat_tomb[1],
                        "ev": horoszkop_adat_tomb[2],
                        "honap": horoszkop_adat_tomb[3],
                        "nap": horoszkop_adat_tomb[4],
                        "ora": horoszkop_adat_tomb[5],
                        "perc": horoszkop_adat_tomb[6],
                        "hely": horoszkop_adat_tomb[7]
                    }

                    

    except FileNotFoundError as e:
        print(e, "nem talalja a file beolvasahoz szukseges adatokat az osszes szuletesi adat kigyujtesenel")


def create_uj_horoszkop(nev, hely, horoszkoptipus, ev, honap, nap, ora, perc):
    return {
        "nev": nev,
        "horoszkoptipus": horoszkoptipus,
        "ev": ev,
        "honap": honap,
        "nap": nap,
        "ora": ora,
        "perc": perc,
        "hely": hely
    }


def create_szuletesi_keplet(nev, hely, ev, honap, nap, ora, perc):
    return create_uj_horoszkop(nev, hely, "radix", ev, honap, nap, ora, perc)


def horoszkop_feltoltese_csvbe(horoszkopadatok: dict):
    try:
        with open("../kepletek/szuletesi_adatok.csv", "a") as f:
            # todo append + join a tombbel h ne legyen a sor vegen null
            for k, v in horoszkopadatok.items():
                f.write(str(v) + ";")
            f.write("\n")
    except FileNotFoundError as e:
        print(e, "nem talalja a file beolvasahoz szukseges adatokat az osszes szuletesi adat kigyujtesenel")


#horoszkop_feltoltese_csvbe(create_szuletesi_keplet("adam", "Szolnok", 2001, 8, 19, 16, 19))


#print(get_szuletesi_adat_nev_alapjan("adam"))
# todo duplikalt szuletesi adatok szurese
