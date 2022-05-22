import datetime
import json
import sqlite3


def beolvasas_csv():
    adatok = []
    with open("Asztrológia hivatás adatok - Munkalap1.tsv") as f:
        f.readline()
        for i in f:
            a = i.strip().split("\t")
            a.pop(0)
            if len(a) != 0:
                row = {}
                dte = a[0].strip().replace(":", ".").split(".")
                dte = [int(i) for i in dte]
                while len(dte) < 6:
                    dte.append(0)

                row["datumido"] = datetime.datetime(year=dte[0],
                                                    month=dte[1],
                                                    day=dte[2],
                                                    hour=dte[3],
                                                    minute=dte[4],
                                                    second=dte[5])
                row["hely"] = a[1]
                row["nev"] = a[3]
                row["munka"] = {"munkak": [i for i in a[2].split(",")]}
                if a[3].lower().strip() == "nő" or a[3].lower().strip() == "férfi":
                    row["neme"] = a[3]
                    row["nev"] = "-"
                else:
                    row["neme"] = "-"
                    row["nev"] = a[3]

                adatok.append(row)

    return adatok


def beolvasas_json(json_file_name):
    adatok = []

    with open(json_file_name) as json_file:
        adatbazis = json.load(json_file)

        print(adatbazis)
        for row in adatbazis["horoszkopok"]:
            uj_adatosor = {}
            print(row)
            uj_adatosor["datumido"] = datetime.datetime(year=int(row["ev"]),
                                                        month=int(row["honap"]),
                                                        day=int(row["nap"]),
                                                        hour=int(row["ora"]),
                                                        minute=int(row["perc"]),
                                                        second=int(row["mp"]))
            uj_adatosor["hely"] = row["hely"]
            uj_adatosor["nev"] = row["nev"]
            uj_adatosor["munka"] = {"munkak": row["munka"]}
            uj_adatosor["neme"] = row["neme"]

            adatok.append(uj_adatosor)
    print(adatok)
    return adatok


def main():
    conn = sqlite3.connect("../../weboldal/db2.sqlite3")
    c = conn.cursor()
    eltolas = 1

    alapadatok_from_csv = beolvasas_csv()
    alapadatok_from_json = beolvasas_json("horoszkopok.json")
    alapadatok = alapadatok_from_json + alapadatok_from_csv


    records = []
    for i, adat in enumerate(alapadatok, eltolas):
        print(alapadatok)
        records.append((i, adat["nev"], adat["datumido"], adat["hely"],
                        "radix", adat["neme"], "{}",
                        str(adat["munka"]).replace("'", "$").replace('"', "'").replace("$", '"')))

    print(records)
    # insert multiple records in a single query
    c.executemany('INSERT INTO base_horoszkopalapadat VALUES(?,?,?,?,?,?,?,?);', records);
    # k= c.execute('select * from base_horoszkopalapadat;')
    # print(k.description)

    print('We have inserted', c.rowcount, 'records to the table.')

    # commit the changes to db
    conn.commit()
    # close the connection
    conn.close()


if __name__ == '__main__':
    main()
    # beolvasas_json("horoszkopok.json")
