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


def decision_tree(ohe_features,labels,i):

    dt = tree.DecisionTreeClassifier(max_depth=6) # legfeljebb 3 mély fát építhet
    dt.fit(ohe_features, labels)
    prediction = dt.predict(ohe_features)
    print(prediction)
    from sklearn.metrics import accuracy_score
    acc = accuracy_score(prediction, labels)
    print(acc)

    fig = plt.figure(figsize=(25,20))
    _ = tree.plot_tree(dt,filled=True)
    fig.savefig(f"dt_pics/decistion_tree_{i}.png")

    return acc
