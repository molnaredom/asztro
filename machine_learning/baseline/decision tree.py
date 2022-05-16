import pandas as pd
import pandas
from sklearn import tree
import pydotplus
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
data_top = df.head()



feature_names = list(df.columns)

categorical_adatok = feature_names
categorical_adatok.remove("Életkor")
# print(categorical_adatok)

df[categorical_adatok] =\
    df[categorical_adatok].astype('category')
#
# pd.get_dummies(data=data, columns=['Name'])

df.apply(pd.to_numeric)
#
# print(features.dtypes)


dtree = DecisionTreeClassifier()
dtree = dtree.fit(features, labels)
data = tree.export_graphviz(dtree, out_file=None, feature_names=feature_names)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('mydecisiontree.png')

img=pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show()


