import pandas
import pandas as pd

from machine_learning.baseline.munka_osztalyozo import munka_osztalyozas

df = pandas.read_csv("../kinyert_adatok.csv", sep=";")

# az első sor csk aindexeket tartalmaz ezért ezt vegyük ki a dataframeből
del df[df.columns[0]]

print(f"Összes adat {len(df)}")

# Távolítsuk el azokat a sorokat amelyek még nem rendelkeznek munkával
df = df.drop(df[df["Munka"] == "[]"].index)
df = df.drop(df[df["Munka"] == "['?']"].index)
df = df.drop(df[df["Munka"] == "['']"].index)

# amennyiben egy embernek több munkája is van azokat szedjük szét külön egyedekre
# ezáltal várhatóan nőni fog az adathalmaz mértéke

uj_df = pd.DataFrame()
for idx, row in df.iterrows():
    for munka in eval(row["Munka"]):
        row["Munka"] = munka
        uj_df = uj_df.append(row, ignore_index = True)

df = uj_df
print(f"Munkákhoz rendelt horoszkópok száma {len(df)}")

# munkák osztályozása egy megadott szempont szerint
# minden munkához egy egy számértéket rendelünk
osztalyozo = munka_osztalyozas(irodai=True)
df['Munka'] = df['Munka'].map(osztalyozo)
df.dropna(subset=['Munka']) # todo nem dobja el a nan ertekeket
print(df)

print(f"Osztályozott munkákhoz rendelt horoszkópok száma {len(df)}")

