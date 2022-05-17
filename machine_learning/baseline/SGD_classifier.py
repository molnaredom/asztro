import pandas as pd
import pandas
from pydotplus import graphviz
from sklearn import tree
import pydotplus
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

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
df.dropna(inplace=True) # inplace nelkul nem mukodik

print(f"Osztályozott munkákhoz rendelt horoszkópok száma {len(df)}")

print(df["Munka"].hist())

labels = df.pop("Munka")
features = df

# print(labels)
# print(features)


# feature_names = features.columns
# categorical_adatok = feature_names
# # categorical_adatok.remove("Életkor")
# print(categorical_adatok)

# df[categorical_adatok] =\
#     df[categorical_adatok].astype('category')
# #
# pd.get_dummies(data=data, columns=['Name'])

# df.apply(pd.to_numeric)


from sklearn import preprocessing
ohe = preprocessing.OneHotEncoder() #one hot encoding
# vessszük az összes adatot, ami nem float/int, vagyis object (categorical) változó
categorical_features = ohe.fit_transform(features.select_dtypes(include=['object']))
neme = ohe.fit_transform(features[["Neme"]])


# print(neme.toarray())
print("shape neme:", neme.shape)

import scipy.sparse
numeric_features = scipy.sparse.csr_matrix(features.select_dtypes(exclude=['object'])) # numerikus jellemzők ritka mátrixként

ohe_features = scipy.sparse.hstack((categorical_features, numeric_features)) # ritka mátrixok horizontális konkatenálása
# print(ohe_features.toarray())

with open("k.txt", "w") as f:
    for i in ohe_features.toarray():
        f.write(str(i))


features = ohe_features
print("shape:", categorical_features.shape)


from sklearn.linear_model import SGDClassifier

cls = SGDClassifier()

# a features a tanító adatbázis egyedeinek jellemzőreprezentációja, ami ugyanolyan hosszú, mint a címkevektor (a célváltozó ami a tanító példa)
model = cls.fit(features, labels)

from sklearn.metrics import accuracy_score, classification_report

prediction = model.predict(features)
print(prediction) # a predikció eredménye egy lista az egyedekre predikált címkékkel

acc =accuracy_score(y_true=labels, y_pred=prediction)
print(acc)
print(classification_report(y_true=labels, y_pred=prediction))
