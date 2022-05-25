from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score, classification_report, f1_score
import matplotlib.pyplot as plt
from skopt import BayesSearchCV
from sklearn.linear_model import SGDClassifier


def sgd_classifier(train_features, valid_features, train_classlabels, valid_classlabels):

    model_param = {
        'penalty': ['l2', 'l1', 'elasticnet'],
        'l1_ratio': [0.0, 0.1, 0.2, 0.5, 0.8, 0.9, 0.95, 1.0],
        'loss': ['hinge', 'log', 'modified_huber', 'squared_hinge', 'perceptron', 'squared_loss', 'huber',
                 'epsilon_insensitive', 'squared_epsilon_insensitive'],
        'alpha': [10 ** x for x in range(-6, 1)],
        'random_state': [0]
    }

    valid_f1 = []
    train_f1 = []
    for c in model_param["loss"]:
        # for d in model_param["alpha"]:
        for a in model_param["penalty"]:
            for b in model_param["l1_ratio"]:

                cls = SGDClassifier(random_state=0,
                                    max_iter=100000,
                                    penalty=a,
                                    l1_ratio=b,
                                    loss=c,
                                    # alpha=d
                                    )
                cls.fit(train_features, train_classlabels)
                valid_prediction = cls.predict(valid_features)
                valid_f1.append(f1_score(valid_classlabels, valid_prediction, pos_label=1))
                train_prediction = cls.predict(train_features)
                train_f1.append(f1_score(train_classlabels, train_prediction, pos_label=1))


            plt.figure(figsize=(10, 10))
            plt.title(f"SGD Classifier penalty:{a} l1_ratio:{b} loss:{c}")
            plt.plot(valid_f1, c="green")
            plt.plot(train_f1, c="red")
            plt.ylabel("F1 score")
            plt.xlabel("Regularizációs együttható")
            plt.show()
            valid_f1 = []
            train_f1 = []

    return 1

