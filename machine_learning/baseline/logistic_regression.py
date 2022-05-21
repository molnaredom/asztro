from sklearn.metrics import f1_score
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt


def logreg(train_features, valid_features, train_classlabels, valid_classlabels):
    valid_f1 = []
    train_f1 = []
    for l in range(-7, 5):
        lin = LogisticRegression(random_state=0,
                                 max_iter=100000,
                                 # nehéz feladat a lineáris gépnek, engedjük a defaultnál tovább tanulni
                                 class_weight="",
                                 # tanulásnál átsúlyozzuk a ritka osztálycímkéket, ez sokat segít lineáris gépeknél
                                 C=10 ** l)  # regularizációs együttható
        lin.fit(train_features, train_classlabels)
        valid_prediction = lin.predict(valid_features)
        valid_f1.append(f1_score(valid_classlabels, valid_prediction, pos_label=1))
        train_prediction = lin.predict(train_features)
        train_f1.append(f1_score(train_classlabels, train_prediction, pos_label=1))

    plt.figure(figsize=(10, 10))
    plt.title("Non Balanced LogReg")
    plt.plot(valid_f1, c="green")
    plt.plot(train_f1, c="red")
    plt.ylabel("F1 score")
    plt.xlabel("Regularizációs együttható")
    plt.show()

    for l in range(-7, 5):
        lin = LogisticRegression(random_state=0,
                                 max_iter=100000,
                                 # nehéz feladat a lineáris gépnek, engedjük a defaultnál tovább tanulni
                                 class_weight="balenced",
                                 # tanulásnál átsúlyozzuk a ritka osztálycímkéket, ez sokat segít lineáris gépeknél
                                 C=10 ** l)  # regularizációs együttható
        lin.fit(train_features, train_classlabels)
        valid_prediction = lin.predict(valid_features)
        valid_f1.append(f1_score(valid_classlabels, valid_prediction, pos_label=1))
        train_prediction = lin.predict(train_features)
        train_f1.append(f1_score(train_classlabels, train_prediction, pos_label=1))


    plt.figure(figsize=(10, 10))
    plt.title("Balanced LogReg")
    plt.plot(valid_f1, c="green")
    plt.ylabel("F1 score")
    plt.xlabel("Regularizációs együttható (-7+x)^10")
    plt.plot(train_f1, c="red")
    plt.show()
