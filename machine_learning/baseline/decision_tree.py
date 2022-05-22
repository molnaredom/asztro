import pandas as pd
import pandas
from pydotplus import graphviz
from sklearn import tree
import pydotplus
from sklearn.metrics import f1_score, classification_report
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

from machine_learning.baseline.munka_osztalyozo import munka_osztalyozas


def decision_tree(train_features, valid_features, train_classlabels, valid_classlabels):
    valid_f1 = []
    train_f1 = []
    for d in range(1, 40):
        dt = tree.DecisionTreeClassifier(max_depth=d)  # döntési fa mélysége
        dt.fit(train_features, train_classlabels)  # tanítunk a tanító adatbázison
        valid_prediction = dt.predict(valid_features)
        valid_f1.append(f1_score(valid_classlabels, valid_prediction, pos_label=1))  # kiértékelés a validációs halmazon
        train_prediction = dt.predict(train_features)
        train_f1.append(f1_score(train_classlabels, train_prediction,
                                 pos_label=1))  # a tanító adatbázison is kiértékeljük a túltanulási vizsgálatokhoz

    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 10))
    plt.plot(valid_f1, c="green")
    plt.plot(train_f1, c="red")
    plt.show()

    #
    # dt = tree.DecisionTreeClassifier(max_depth=6) # legfeljebb 3 mély fát építhet
    # dt.fit(ohe_features, labels)
    # prediction = dt.predict(ohe_features)
    # print(prediction)
    # from sklearn.metrics import accuracy_score
    # acc = accuracy_score(prediction, labels)
    # print(acc)
    #
    # fig = plt.figure(figsize=(25,20))
    # _ = tree.plot_tree(dt,filled=True)
    # fig.savefig(f"dt_pics/decistion_tree_{i}.png")
