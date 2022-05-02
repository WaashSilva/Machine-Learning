import numpy as np
data = [15, 16, 18, 19, 22, 24, 29, 30, 34]
print('media:',np.mean(data))
print('mediana:',np.median(data))
print('50th percentile(median):',
      np.percentile (data,50))
print('25th percentile(median):',
      np.percentile (data,25))
print('75th percentile(median):',
      np.percentile (data,75))
print('desvio padrão:',np.std(data))
print('variancia:',np.var(data))


import pandas as pd
df = pd.read_csv ('https://sololearn.com/uploads/files/titanic.csv')
col = df['Fare']
print (col)

# Agora usamos essa lista dentro da notação de colchetes df[...] Ao imprimir um DataFrame grande 
# demais para ser exibido, você pode usar o método head para imprimir apenas as 5 primeiras linhas.
# small_df = df[ ]
# print(small_df.head())['Idade', 'Sexo', 'Sobreviveu']

import pandas as pd
df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
small_df = df [['Age', 'Sex', 'Survived']]
print (small_df.head())

# Criamos uma Série de Pandas que será uma série de Verdadeiros e Falsos (True se o passageiro 
# for homem e False se o passageiro for mulher ).
#EXEMPLO
import pandas as pd
df = pd.read_csv ('https://sololearn.com/uploads/files/titanic.csv')
df ['male'] = df['Sex'] == 'male'
print (df.head())

# Muitas vezes começamos com nossos dados em um Pandas DataFrame, mas depois queremos convertê-los
# em uma matriz numpy. O atributo values ​​faz isso por nós. Vamos converter a coluna Fare em um array numpy
# Primeiro, lembramos que podemos usar a notação de colchete único para obter uma série de pandas da
# coluna Fare da seguinte maneira.
import pandas as pd
df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
print (df['Fare'].values)

#Se tivermos um DataFrame pandas (em vez de um Series como na última parte), ainda podemos usar o atributo
# values, mas ele retorna um . Lembre-se de que podemos criar um DataFrame de pandas menor com a seguinte
# sintaxe.matriz numpy bidimensional
import pandas as pd
df = pd.read_csv ('https://sololearn.com/uploads/files/titanic.csv')
print (df[['Pclass', 'Fare','Age']].values)

# Usamos o atributo de SHAPE numpy para determinar o tamanho do nosso array numpy. O tamanho nos diz quantas
# linhas e colunas existem em nossos dados. Primeiro, vamos criar um array numpy com Pclass, Fare e Age.
import pandas as pd
df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
arr = df[['Pclass', 'Fare', 'Age']].values
print (arr.shape)

# Para selecionar uma única coluna (neste caso a coluna Idade), temos que usar alguma sintaxe especial:
import pandas as pd
df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
arr = df[['Pclass', 'Fare','Age']].values
print(arr[0, 1]) # valor unico
print(arr[0]) # linha inteira
print(arr[:,2]) # coluna inteira

# Muitas vezes você deseja selecionar todas as linhas que atendem a determinados critérios. Neste exemplo,
# selecionaremos todas as linhas de crianças (passageiros com menos de 18 anos). Um lembrete de nossa
# definição de array:
import pandas as pd
df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
arr = df [['Pclass', 'Fare', 'Age']].values[:10]
mask = arr[:,2] < 18
print (arr[mask])
print (arr[arr[:,2] < 18 ])


# Digamos que queremos saber quantos de nossos passageiros são crianças. Ainda temos a mesma definição
# de array e podemos pegar nossos valores de máscara ou booleanos da parte anterior.
import pandas as pd
df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
arr = df [['Pclass', 'Fare', 'Age']].values[:10]
mask = arr[:,2] < 18
print (arr[mask])
print (arr[arr[:,2] < 18 ].sum())


# Usando matplotlib para graficos
import matplotlib.pyplot as plt
plt.scatter(df['Fare'],df['Pclass'],c=df['Survived'])
plt.xlabel('Fare')
plt.ylabel('Pclass')

# Obtendo uma coluna de uma matriz numpy. Tarefa Dado um arquivo csv e um nome 
# de coluna, imprima os elementos na coluna fornecida. Formato de entrada Primeira
# linha: nome do arquivo de um arquivo csv Segunda linha: nome da coluna Formato 
#de saída Array Numpy Exemplo de entrada https://sololearn.com/uploads/files/one.csv 
#a Arquivo one.csv contents: a,b 1,3 2 ,4 Saída de Amostra [1 2]
filename = input()
column_name = input()
import pandas as pd
df=pd.read_csv(filename)
arr=df[column_name].values
print(arr)
































































































































































