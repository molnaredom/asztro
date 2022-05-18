from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score, classification_report


def sgd_classifier(features, labels):
    cls = SGDClassifier()

    # a features a tanító adatbázis egyedeinek jellemzőreprezentációja,
    # ami ugyanolyan hosszú, mint a címkevektor (a célváltozó ami a tanító példa)
    model = cls.fit(features, labels)

    prediction = model.predict(features)
    print(prediction) # a predikció eredménye egy lista az egyedekre predikált címkékkel

    acc = accuracy_score(y_true=labels, y_pred=prediction)
    print(acc)
    print(classification_report(y_true=labels, y_pred=prediction))
    return acc

