from numpy import mean
from numpy import absolute
from numpy import sqrt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression


def kfold(features, labels):
    accs = []
    for n_split in range(4,15):
        cv = KFold(n_splits=n_split, random_state=1, shuffle=True)
        model = LinearRegression()
        scores = cross_val_score(model, features, labels, scoring='neg_mean_squared_error',
                                 cv=cv, n_jobs=-1)
        # print(scores)
        acc =sqrt(mean(absolute(scores)))
        accs.append(acc)

    print(accs)
    print(mean(accs))
    return mean(accs)
