import numpy as np
import pandas as pd
import statistics as stat
from prettytable import PrettyTable

col_list = ["Sepal length", "Sepal width", "Petal length",
            "Petal width", "Species"]

Dataframe = pd.read_csv('data.csv', header=None, names=col_list)
Occurrences_list = Dataframe['Species'].values.tolist()
Sepal_length_list = Dataframe['Sepal length'].values.tolist()
Sepal_width_list = Dataframe['Sepal width'].values.tolist()
Petal_length_list = Dataframe['Petal length'].values.tolist()
Petal_width_list = Dataframe['Petal width'].values.tolist()

if __name__ == "__main__":
    # print(Dataframe)

    # poniewaz 0 w arkuszu csv oznacza Setose, 1 Versicolore, 2 Virginice
    Setoses = Occurrences_list.count(0)
    Versicolors = Occurrences_list.count(1)
    Virginicas = Occurrences_list.count(2)

    PercentageOccurrenceSet = Setoses/len(Occurrences_list)
    PercentageOccurrenceVers = Versicolors/len(Occurrences_list)
    PercentageOccurrenceVirg = Virginicas/len(Occurrences_list)

    # wartosci skrajne min i max

    sepal_length_min = min(Sepal_length_list)
    sepal_width_min = min(Sepal_width_list)
    petal_length_min = min(Petal_length_list)
    petal_width_min = min(Petal_width_list)

    sepal_length_max = max(Sepal_length_list)
    sepal_width_max = max(Sepal_width_list)
    petal_length_max = max(Petal_length_list)
    petal_width_max = max(Petal_width_list)

    print(sepal_length_min)
    print(sepal_length_max)
    print(sepal_width_min)
    print(sepal_width_max)
    print()
    print(petal_length_min)
    print(petal_length_max)
    print(petal_width_min)
    print(petal_width_max)

    # miary tendencji centralnej: średnia arytmetyczna, mediana

    sepal_length_mean = stat.mean(Sepal_length_list)
    sepal_width_mean = stat.mean(Sepal_width_list)
    petal_length_mean = stat.mean(Petal_length_list)
    petal_width_mean = stat.mean(Petal_width_list)
    print()
    sepal_length_median = stat.median(Sepal_length_list)
    sepal_width_median = stat.median(Sepal_width_list)
    petal_length_median = stat.median(Petal_length_list)
    petal_width_median = stat.median(Petal_width_list)

    print(sepal_length_mean)
    print(sepal_width_mean)
    print(petal_length_mean)
    print(petal_width_mean)
    print()
    print(sepal_length_median)
    print(sepal_width_median)
    print(petal_length_median)
    print(petal_width_median)
    print()
    # miary położenia wyższych rzędów: dolny kwartyl (Q1), górny kwartyl (Q3)
    # quantile z numpy quantile(tablica, .kwantyl)

    sepal_length_q1 = np.quantile(Sepal_length_list, .25)
    sepal_length_q3 = np.quantile(Sepal_length_list, .75)

    sepal_width_q1 = np.quantile(Sepal_width_list, .25)
    sepal_width_q3 = np.quantile(Sepal_width_list, .75)

    petal_length_q1 = np.quantile(Petal_length_list, .25)
    petal_length_q3 = np.quantile(Petal_length_list, .75)

    petal_width_q1 = np.quantile(Petal_width_list, .25)
    petal_width_q3 = np.quantile(Petal_width_list, .75)

    print(sepal_length_q1)
    print(sepal_length_q3)
    print(sepal_width_q1)
    print(sepal_width_q3)
    print()
    print(petal_length_q1)
    print(petal_length_q3)
    print(petal_width_q1)
    print(petal_width_q3)
    print()

    # miara zróżnicowania rozkładu: odchylenie standardowe (obliczona ze wzoru dla próby).
    # metoda std z biblioteki numpy.std(a, axis=None, dtype=None, out=None, ddof=0, keepdims=<no value>)

    sepal_length_std_dev = np.std(Sepal_length_list)
    sepal_width_std_dev = np.std(Sepal_width_list)

    petal_length_std_dev = np.std(Petal_length_list)
    petal_width_std_dev = np.std(Petal_width_list)

    print(sepal_length_std_dev)
    print(sepal_width_std_dev)
    print()
    print(petal_length_std_dev)
    print(petal_length_std_dev)

    table = PrettyTable()
    column_names = ['Cecha','Minimum','Śr.arytm.(± odch.stand.)','Mediana(Q1 - Q3)','Maksimum']
    table.add_column(column_names[0],["Długość działki kielicha (cm)", "Szerokość działki kielicha (cm)", "Długość płatka (cm)", "Szerokość płatka (cm)"])
    table.add_column(column_names[1],[sepal_length_min, sepal_width_min, petal_length_min, petal_width_min])
    print(table)