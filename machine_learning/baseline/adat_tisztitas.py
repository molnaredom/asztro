import pandas as pd
import pandas
from machine_learning.baseline.munka_osztalyozo import munka_osztalyozas
from sklearn import preprocessing
import scipy.sparse

def adat_tisztito(df:pandas.DataFrame, osztalyozas_tipus):

    print(f"Összes adat {len(df)}")

    # az első sor csak indexeket tartalmaz ezért ezt vegyük ki a dataframeből
    del df[df.columns[0]]

    # Távolítsuk el azokat a sorokat(embereket) amelyek még nem rendelkeznek munkával,vagy nem rendelkezünk adattal róla
    df = df.drop(df[df["Munka"] == "[]"].index)
    df = df.drop(df[df["Munka"] == "['?']"].index)
    df = df.drop(df[df["Munka"] == "['']"].index)
    print("Munkával rendelkező emberek száma:", len(df))

    # amennyiben egy embernek több munkája is van azokat szedjük szét külön egyedekre
    # például ha egy ember 3 munkával rendelkezik, akkor az 1 ember 3 horoszkópra fog bombali,
    # azonos horoszkópok, különböző munka -- Lényeg hogy 1 horoszkóp 1 munka legyen
    # ezáltal várhatóan nőni fog az adathalmaz

    tmp_df = pd.DataFrame()
    for idx, row in df.iterrows():
        for munka in eval(row["Munka"]):
            row["Munka"] = munka
            tmp_df = tmp_df.append(row, ignore_index = True)
    df = tmp_df
    print(f"Munkákhoz rendelt horoszkópok száma {len(df)}")

    # munkák osztályozása egy megadott szempont szerint
    # minden munkához egy egy számértéket rendelünk
    osztalyozo = munka_osztalyozas(oszatlozas_alap=osztalyozas_tipus)
    df['Munka'] = df['Munka'].map(osztalyozo)
    df.dropna(inplace=True) # inplace nelkul nem mukodik

    print(f"Osztályozott munkákhoz rendelt horoszkópok száma {len(df)}")

    class_labels = df.pop("Munka")
    features = df


    ohe = preprocessing.OneHotEncoder()  # one hot encoding
    # vessszük az összes adatot, ami nem float/int, vagyis object (categorical) változó
    categorical_features = ohe.fit_transform(features.select_dtypes(include=['object']))

    numeric_features = scipy.sparse.csr_matrix(
        features.select_dtypes(exclude=['object']))  # numerikus jellemzők ritka mátrixként

    ohe_features = scipy.sparse.hstack(
        (categorical_features, numeric_features))  # ritka mátrixok horizontális konkatenálása
    # print(ohe_features.toarray())

    with open("k.txt", "w") as f:
        for i in ohe_features.toarray():
            f.write(str(i))

    features = ohe_features
    print("One hot encode-olt adattábla alakja (sor, oszlop):", categorical_features.shape)

    return class_labels, features
