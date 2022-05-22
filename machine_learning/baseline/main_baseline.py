import numpy
import pandas

from machine_learning.baseline.SGD_classifier import sgd_classifier
from machine_learning.baseline.adat_tisztitas import *

import argparse

from machine_learning.baseline.compare import compare
from machine_learning.baseline.decision_tree import decision_tree
from machine_learning.baseline.k_fold_cross_validation import kfold
from machine_learning.baseline.logistic_regression import logreg

parser = argparse.ArgumentParser()

parser.add_argument("-m", "--mode", default="SGD",
                    help="Set running mode: SGD, DT, KFOLD, LOGREG")

args = parser.parse_args()


def main():
    df = pandas.read_csv("../kinyert_adatok.csv", sep=";")
    train_features, valid_features, train_classlabels, valid_classlabels  = adat_tisztito(df, osztalyozas_tipus= "irodai")

    if "SGD" in args.mode:
        print("SGD classifier started")
        sgd_classifier(train_features, valid_features, train_classlabels, valid_classlabels)

    if "DT" in args.mode:
        print("Decision Tree started")
        decision_tree(train_features, valid_features, train_classlabels, valid_classlabels)

    if "KFOLD" in args.mode:
        print("K-Fold cross validation started")
        kfold(train_features, valid_features, train_classlabels, valid_classlabels)

    if "LOGREG" in args.mode:
        print("Logistic Regression started")
        logreg(train_features, valid_features, train_classlabels, valid_classlabels)

    if "COMPARE" in args.mode:
        print("Logistic Regression started")
        compare(train_features, valid_features, train_classlabels, valid_classlabels)


if __name__ == '__main__':
    main()
