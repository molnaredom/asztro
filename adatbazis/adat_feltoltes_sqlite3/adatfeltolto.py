import datetime
import sqlite3


def beolvasas():
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
                if a[3].lower() == "nő" or a[3].lower() == "férfi":
                    row["neme"] = a[3]
                    row["nev"] = "-"
                else:
                    row["neme"] = "-"
                    row["nev"] = a[3]

                adatok.append(row)

    return adatok


def main():
    conn = sqlite3.connect("../../weboldal/db2.sqlite3")
    c = conn.cursor()
    eltolas = 1

    # records or rows in a list

    alapadatok = beolvasas()
    records = []
    for i, adat in enumerate(alapadatok, eltolas):
        records.append((i,adat["nev"], adat["datumido"], adat["hely"],
                        "radix", adat["neme"], "{}",
                        str(adat["munka"]).replace("'", "$").replace('"', "'").replace("$",'"')))

    print(records)
    # records = [(4, 'Abraham Lincoln', datetime.datetime(1809, 2, 12, 18, 37), "Hotgenville", "radix",
    #             "férfi", '{"helo": "hi"}', '{"munkak": ["Elnök"]}')]
    # records = [(5, 'M. Ádám', datetime.datetime(2001, 8, 19, 16, 54, 23), 'Szolnok', 'radix',
    #             '-', '{"hello": "s"}', '{"munka": ["informatika(programozó)", " vendéglátás(pénztáros)"]}')]

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
# main()
