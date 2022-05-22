import pandas as pd
import pandas
from machine_learning.baseline.munka_osztalyozo import munka_osztalyozas
from sklearn import preprocessing
import scipy.sparse
from sklearn.model_selection import train_test_split

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
    for idx, row in df.iterrows():  # egyes embereken cégigiterál
        # print(idx)
        for munka in eval(row["Munka"]):  # emberek munkáin végigiterál
            row["Munka"] = munka.lower().strip()
            # print("   ",row["Munka"] )
            tmp_df = tmp_df.append(row, ignore_index = True)
    df = tmp_df
    print(f"Munkákhoz rendelt horoszkópok száma {len(df)}")

    # munkák osztályozása egy megadott szempont szerint
    # minden munkához egy egy számértéket rendelünk
    osztalyozo = munka_osztalyozas(oszatlozas_alap=osztalyozas_tipus)
    # [print(i) for i in df['Munka'].iteritems()]
    df['Munka'] = df['Munka'].map(osztalyozo)
    # [print(i) for i in df['Munka'].iteritems()]
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

    train_features, valid_features, train_classlabels, valid_classlabels = train_test_split(features, class_labels,
                                                                                            test_size=0.25,
                                                                                            random_state=42)

    print(f"\n{train_features=}\n, {valid_features=}\n, {train_classlabels=}\n, {valid_classlabels=}")
    # class_labels.hist()


    from matplotlib import pyplot as plt
    import numpy as np
    # A dataset of 10 students
    # plt.show()

    return train_features, valid_features, train_classlabels, valid_classlabels
