import numpy
import pandas

from machine_learning.baseline.SGD_classifier import sgd_classifier
from machine_learning.baseline.adat_tisztitas import *

import argparse

from machine_learning.baseline.decision_tree import decision_tree

parser = argparse.ArgumentParser()

parser.add_argument("-m", "--mode", default="SGD",
                    help="Set running mode, SGD, DT")

args = parser.parse_args()


def main():
    df = pandas.read_csv("../kinyert_adatok.csv", sep=";")
    class_labels, features = adat_tisztito(df, osztalyozas_tipus= "irodai")

    pontossagok = []

    if "SGD" in args.mode:
        print("SGD classifier started")
        for _ in range(10):
            acc = sgd_classifier(features, class_labels)
            pontossagok.append(acc)

    if "DT" in args.mode:
        print("Decision Tree started")
        for i in range(1):
            acc = decision_tree(features, class_labels,i)
            pontossagok.append(acc)

    print(pontossagok)
    print("Átlag teljesítmény: ",round(float(numpy.mean(pontossagok)*100),3) , "%", sep="")


if __name__ == '__main__':
    main()
