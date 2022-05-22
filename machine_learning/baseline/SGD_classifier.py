from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score, classification_report, f1_score
import matplotlib.pyplot as plt
from skopt import BayesSearchCV
from sklearn.linear_model import SGDClassifier


def sgd_classifier(train_features, valid_features, train_classlabels, valid_classlabels):
    model = SGDClassifier()
    print(train_features)

    model_param = {
        'penalty': ['l2', 'l1', 'elasticnet'],
        'l1_ratio': [0.0, 0.05, 0.1, 0.2, 0.5, 0.8, 0.9, 0.95, 1.0],
        'loss': ['hinge', 'log', 'modified_huber', 'squared_hinge', 'perceptron', 'squared_loss', 'huber',
                 'epsilon_insensitive', 'squared_epsilon_insensitive'],
        'alpha': [10 ** x for x in range(-6, 1)],
        'random_state': [0]
    }

    opt = BayesSearchCV(model, model_param, n_iter=32, cv=3)
    opt.fit(train_features, train_classlabels)
    opt_pred_values = opt.predict(valid_features)

    clfrep = classification_report(valid_classlabels, opt_pred_values)
    print(clfrep)


    print(opt_pred_values)
    exit()
    valid_f1 = []
    train_f1 = []
    for l in range(-7, 5):
        cls = SGDClassifier(random_state=0,
                                 max_iter=100000,
                                 class_weight="",
                                 )
        cls.fit(train_features, train_classlabels)
        valid_prediction = cls.predict(valid_features)
        valid_f1.append(f1_score(valid_classlabels, valid_prediction, pos_label=1))
        train_prediction = cls.predict(train_features)
        train_f1.append(f1_score(train_classlabels, train_prediction, pos_label=1))

    plt.figure(figsize=(10, 10))
    plt.title("Non Balanced LogReg")
    plt.plot(valid_f1, c="green")
    plt.plot(train_f1, c="red")
    plt.ylabel("F1 score")
    plt.xlabel("Regularizációs együttható")
    plt.show()

    cls = SGDClassifier()

    # a features a tanító adatbázis egyedeinek jellemzőreprezentációja,
    # ami ugyanolyan hosszú, mint a címkevektor (a célváltozó ami a tanító példa)
    model = cls.fit(features, labels)

    prediction = model.predict(features)
    print(prediction) # a predikció eredménye egy lista az egyedekre predikált címkékkel

    acc = accuracy_score(y_true=labels, y_pred=prediction)
    print(acc)
    # print(classification_report(y_true=labels, y_pred=prediction))
    return round(acc, 3)

