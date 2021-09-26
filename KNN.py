#Base de dados:#https://archive.ics.uci.edu/ml/datasets/wine – UCI machine learning repository.

#https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html#sklearn.datasets.load_wine – módulo do Sklearn que possui alguns conjuntos de dados.

#Aplicando o KNN na Base de Dados Wine (amostras de vinho)

from sklearn import datasets
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt

wine = datasets.load_wine()

# Criando o DataFrame
df_wine = pd.DataFrame(data=wine.data,columns=wine.feature_names)

# Criando a coluna com os valores da variável target.
df_wine['class'] = wine.target

df_wine.head().T
df_wine['class'].value_counts()

X_train, X_test, y_train, y_test = train_test_split(df_wine.drop('class',axis=1), df_wine['class'], test_size=0.3)
