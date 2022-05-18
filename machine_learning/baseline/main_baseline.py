import numpy
import pandas

from machine_learning.baseline.SGD_classifier import sgd_classifier
from machine_learning.baseline.adat_tisztitas import *

import argparse

parser = argparse.ArgumentParser()

# parser.add_argument("-o", "--Output",
#                     help="Show Output")
parser.add_argument("-m", "--mode", default="SGD",
                    help="Set running mode, SGD, DT")

args = parser.parse_args()


def main():
    df = pandas.read_csv("../kinyert_adatok.csv", sep=";")
    class_labels, features = adat_tisztito(df, osztalyozas_tipus= "irodai")

    pontossagok = []

    if "SGD" in args.mode:

        for i in range(20):
            acc = sgd_classifier(features, class_labels)
            pontossagok.append(acc)

    print(pontossagok)
    print("Átlag teljesítmény:",numpy.mean(pontossagok))


if __name__ == '__main__':
    main()
