import numpy as np
import pandas as pd
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

    PercentageOccurrenceSet = round((Setoses/len(Occurrences_list)) * 100, 2)
    PercentageOccurrenceVers = round((Versicolors/len(Occurrences_list)) * 100, 2)
    PercentageOccurrenceVirg = round((Virginicas/len(Occurrences_list)) * 100, 2)

    # wartosci skrajne min i max
    sepal_length_min = round(min(Sepal_length_list), 2)
    sepal_width_min = round(min(Sepal_width_list), 2)
    petal_length_min = round(min(Petal_length_list), 2)
    petal_width_min = round(min(Petal_width_list), 2)

    sepal_length_max = round(max(Sepal_length_list), 2)
    sepal_width_max = round(max(Sepal_width_list), 2)
    petal_length_max = round(max(Petal_length_list), 2)
    petal_width_max = round(max(Petal_width_list), 2)

    # miary tendencji centralnej: średnia arytmetyczna, mediana, obie funkcje z numpy
    sepal_length_mean = round(np.average(Sepal_length_list), 2)
    sepal_width_mean = round(np.average(Sepal_width_list), 2)
    petal_length_mean = round(np.average(Petal_length_list), 2)
    petal_width_mean = round(np.average(Petal_width_list), 2)

    sepal_length_median = np.median(Sepal_length_list)
    sepal_width_median = np.median(Sepal_width_list)
    petal_length_median = np.median(Petal_length_list)
    petal_width_median = np.median(Petal_width_list)

    # miary położenia wyższych rzędów: dolny kwartyl (Q1), górny kwartyl (Q3)
    # quantile z numpy quantile(tablica, .kwantyl)
    sepal_length_q1 = round(np.quantile(Sepal_length_list, .25), 2)
    sepal_length_q3 = round(np.quantile(Sepal_length_list, .75), 2)

    sepal_width_q1 = round(np.quantile(Sepal_width_list, .25), 2)
    sepal_width_q3 = round(np.quantile(Sepal_width_list, .75), 2)

    petal_length_q1 = round(np.quantile(Petal_length_list, .25), 2)
    petal_length_q3 = round(np.quantile(Petal_length_list, .75), 2)

    petal_width_q1 = round(np.quantile(Petal_width_list, .25), 2)
    petal_width_q3 = round(np.quantile(Petal_width_list, .75), 2)

    # miara zróżnicowania rozkładu: odchylenie standardowe (obliczona ze wzoru dla próby).
    # metoda std z biblioteki numpy.std(a, axis=None, dtype=None, out=None, ddof=0, keepdims=<no value>)
    sepal_length_std_dev = round(float(np.std(Sepal_length_list)), 2)
    sepal_width_std_dev = round(float(np.std(Sepal_width_list)), 2)

    petal_length_std_dev = round(float(np.std(Petal_length_list)), 2)
    petal_width_std_dev = round(float(np.std(Petal_width_list)), 2)

    # tabelki z biblioteki prettytable
    table1 = PrettyTable()
    column_names1 = ['Gatunek', 'Liczebność (%)']
    table1.add_column(column_names1[0], ['Setosa', 'Versicolor', 'Virginica', 'Razem'])
    table1.add_column(column_names1[1], [str(Setoses) + " (" + str(PercentageOccurrenceSet) + "%)",
                                         str(Versicolors) + " (" + str(PercentageOccurrenceVers) + "%)",
                                         str(Virginicas) + " (" + str(PercentageOccurrenceVirg) + "%)",
                                         str(Setoses + Versicolors + Virginicas) + " (100,0%)"])

    table2 = PrettyTable()
    column_names2 = ['Cecha', 'Minimum', 'Śr.arytm.(± odch.stand.)', 'Mediana(Q1 - Q3)', 'Maksimum']
    table2.add_column(column_names2[0], ["Długość działki kielicha (cm)", "Szerokość działki kielicha (cm)",
                                         "Długość płatka (cm)", "Szerokość płatka (cm)"])
    table2.add_column(column_names2[1], [sepal_length_min, sepal_width_min, petal_length_min, petal_width_min])
    table2.add_column(column_names2[2], [str(sepal_length_mean) + ' (±' + str(sepal_length_std_dev) + ')',
                                         str(sepal_width_mean) + ' (±' + str(sepal_width_std_dev) + ')',
                                         str(petal_length_mean) + ' (±' + str(petal_length_std_dev) + ')',
                                         str(petal_width_mean) + ' (±' + str(petal_width_std_dev) + ')'])
    table2.add_column(column_names2[3], [str(sepal_length_median) + ' (' + str(sepal_length_q1) + ' - ' + str(sepal_length_q3) + ')',
                                         str(sepal_width_median) + ' (' + str(sepal_width_q1) + ' - ' + str(sepal_width_q3) + ')',
                                         str(petal_length_median) + ' (' + str(petal_length_q1) + ' - ' + str(petal_length_q3) + ')',
                                         str(petal_width_median) + ' (' + str(petal_width_q1) + ' - ' + str(petal_width_q3) + ')'])
    table2.add_column(column_names2[4], [sepal_length_max, sepal_width_max, petal_length_max, petal_width_max])

    print(table1.get_string(title="Tabela 1. Liczności gatunków irysów"))
    print(table2.get_string(title="Tabela 2. Charakterystyka cech irysów"))
