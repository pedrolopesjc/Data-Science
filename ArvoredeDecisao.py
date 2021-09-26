#Importa biblioteca
#Importa outras bibliotecas necessárias como pandas, numpy...
from sklearn import tree
#Assume que você tem X (preditor) e Y (alvo) para dados de treino e x_test(predictor) dos dados de teste
# Cria o objeto tree
model = tree.DecisionTreeClassifier(criterion='gini') 
# Para classificação, aqui você pode mudar o algoritmo para gini ou para entropy (Ganho de informação). Por default é gini  
# model = tree.DecisionTreeRegressor() para regressão
# Treina o modelo usando os dados de treino e de teste confere o score
model.fit(X, y)
model.score(X, y)
#Prevê o resultado
predicted= model.predict(x_test)
