import pandas as pd
import nltk
df = pd.DataFrame({‘Aluno’ : [“Wilfred”, “Abbie”, “Harry”, “Julia”, “Carrie”],

  ‘Faltas’ : [3,4,2,1,4],

  ‘Prova’ : [2,7,5,10,6],

  ‘Seminário’: [8.5,7.5,9.0,7.5,8.0]})

tokenizador = nltk.WhitespaceTokenizer()

radicalizador = nltk.RSLPStemmer()

frase = “Amamos muito comer cuscuz todo dia”

frase_tokenizada = tokenizador.tokenize(frase)

palavras_radicalizadas = [ ]

for palavra in frase_tokenizada:

  palavra_radicalizada = radicalizador.stem(palavra)

  palavras_radicalizadas.append(palavra_radicalizada)

 palavras_radicalizadas
  [ ‘am’,  ‘muit’, ‘com’, ‘cuscuz’, ‘tod’, ‘dia’ ]
