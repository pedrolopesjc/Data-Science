# Criar um classificador
nbayes = NBayes::Base.new
# Treinar o classificador com exemplos - as palavras da String são divididas em um array
nbayes.train( "You need to buy some Viagra".split(/\s+/), 'SPAM' )
nbayes.train( "This is not spam, just a letter to Bob.".split(/\s+/), 'HAM' )
nbayes.train( "Hey Oasic, Do you offer consulting?".split(/\s+/), 'HAM' )
nbayes.train( "You should buy this stock".split(/\s+/), 'SPAM' )

# Dividir mensagem que precisa ser classificada
tokens = "Now is the time to buy Viagra cheaply and discreetly".split(/\s+/)
result = @nbayes.classify(tokens)
# Imprime a classe em que o texto foi classificado. (SPAM ou HAM)
p result.max_class
# Imprime a probabilidade da mensagem ser SPAM
p result['SPAM']
# Imprime a probabilidade da mensagem ser HAM
p result['HAM']
