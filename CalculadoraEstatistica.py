'''Neste projeto o estudante deverá individualmente construir um script em Python que receba do usuário duas variáveis de valores referentes
a variáveis quantitativas e devolva como resposta a seguintes medidas de estatística descritiva para cada variável informada: '''

c = 0 # criei um contador para utilizar como parada do laço while

#1°Lista
print("Olá, seja bem vindo a sua calculadora estatistica!")
print("Me chamo Raoni e sou uma calculadora de analise de dados entre 2 listas")
print("Atualmente tenho o limite de 15 indices por lista e ambas devem ter a mesma quantidadr, com isso, por favor...")

while True:
  try:
    n = int(input('Informe a qtde de números inteiros que deseja na lista: '))
    break
  except:
    pass
  print(f'''Cuidado! você não digitou um número inteiro, por favor faça isso''')
numeros = [] #Aqui fica registrado os valores da primeira lista
while c < n:
  try:
    i = int(input(f'Informe o {c+1}º número inteiro da lista: '))
    numeros.append(i)
    c += 1
  except:
    pass
    print(f'''Cuidado! você não digitou um número inteiro, por favor,
    digite o {c+1}º número nvamente''')
d = 0 # criei um contador para utilizar como parada do laço while

#2°Lista
while True:
  try:
    m = int(input('Informe a mesma qtd de números inteiros definida na lista 1: '))
    break
  except:
    pass
  print(f'''Cuidado! você não digitou um número inteiro, por favor faça isso''')
numeros1 = [] #Aqui fica registrado os valores da segunda lista
while d < m:
  try:
    i = int(input(f'Informe o {d+1}º número inteiro da lista: '))
    numeros1.append(i)
    d += 1
  except:
    pass
    print(f'''Cuidado! você não digitou um número inteiro, por favor,
    digite o {d+1}º número nvamente''')
print(numeros)
print(numeros1)

#MÉDIA ARITMÉTICA DA LISTA 1

somal1 = sum(numeros)
medial1 = somal1 / len(numeros)

print("A média Aritmetica da lista 1 é", medial1)

#MÉDIA ARITMÉTICA DA LISTA 2

somal2 = sum(numeros1)
medial2 = somal2 / len(numeros1)
print("A média Aritmetica da lista 2 é", medial2)

#MEDIANA

def mediana(l):
  metade = len(l) // 2
  l.sort()
  if not len(l) % 2:
      return (l[metade - 1] + l[metade]) / 2.0
  return l[metade]

mediana_finalista1 = (mediana(numeros))
mediana_finalista2 = (mediana(numeros1))
print("A mediana da lista 1 é", (mediana(numeros)))
print("A mediana da lista 2 é", (mediana(numeros1)))

#MODA

print("A moda da lista 1 é % s" % (max(set(numeros), key = numeros.count)))

print("A moda da lista 2 é % s" % (max(set(numeros1), key = numeros1.count)))

# VARIÂNCIA

var = sum((l-medial1)**2 for l in numeros) / len(numeros)
var2 = sum((l-medial2)**2 for l in numeros) / len(numeros)

print("A variância da lista 1 é", var)
print("A variância da lista 1 é", var2)

# DESVIO PADRÃO

desviol1 = var ** (1/2)
desviol2 = var2 ** (1/2)

print("O desvio padrão da lista 1 é", desviol1)
print("O desvio padrão da lista 2 é", desviol2)

# Amplitude das listas

# Maior valor da lista1
maxlist1 = max(numeros)
# Menor valor da lista1
minlist1 = min(numeros)

# Maior valor da lista2
maxlist2 = max(numeros1)
# Menor valor da lista2
minlist2 = min(numeros1)

amplitudel1 = maxlist1 - minlist1
amplitudel2 = maxlist2 - minlist2

print("A amplitude da lista 1 é", amplitudel1)
print("A amplitude da lista 2 é", amplitudel2)

#QUARTIL1 DA LISTA 1   == resultado

if len(numeros) <= 3:
  resultado = numeros[0]
  print("O quartil1 da lista 1 é", resultado )
elif len(numeros) == 4:
  resultado = ((numeros[0] + numeros[1]) / 2)
  print("O quartil1 da lista 1 é", resultado)
elif len(numeros) == 5:
  resultado = ((numeros[0] + numeros[1]) / 2)
  print("O quartil1 da lista 1 é", resultado)
elif len(numeros) == 6:
  resultado =  numeros[1]
  print("O quartil1 da lista 1 é", resultado)
elif len(numeros) == 7:
  resultado = numeros[1]
  print("O quartil1 da lista 1 é",resultado)
elif len(numeros) == 8:
  resultado = numeros[1]
  print("O quartil1 da lista 1 é", resultado)
elif len(numeros) == 9:
  resultado = ((numeros[1] + numeros[2]) / 2)
  print("O quartil1 da lista 1 é", resultado)
elif len(numeros) == 10:
  resultado = ((numeros[1] + numeros[2]) / 2 )
  print("O quartil1 da lista 1 é", resultado)
elif len(numeros) == 11:
  resultado = numeros[2]
  print("O quartil1 da lista 1 é", resultado)
elif len(numeros) == 12:
  resultado = ((numeros[2] + numeros[3]) / 2)
  print("O quartil1 da lista 1 é", resultado)
elif len(numeros) == 13:
  resultado = ((numeros[2] + numeros[3]) / 2)
  print("O quartil1 da lista 1 é", resultado)
elif len(numeros) == 14:
  resultado = numeros[3]
  print("O quartil1 da lista 1 é", resultado)
else:
  print("Número maximo de indices excedidos, tente novamente")

#QUARTIL3 DA LISTA 1 == resultado 2

if len(numeros) <= 3:
  resultado2 = numeros[2]
  print("O quartil3 da lista 1 é", resultado2)
elif len(numeros) == 4:
  resultado2 = numeros[3]
  print("O quartil3 da lista 1 é", resultado2)
elif len(numeros) == 5:
  resultado2 = ((numeros[3] + numeros[4]) / 2)
  print("O quartil3 da lista 1 é", resultado2)
elif len(numeros) == 6:
  resultado2 = ((numeros[4] + numeros[5]) / 2)
  print("O quartil3 da lista 1 é", resultado2)
elif len(numeros) == 7:
  resultado2 = numeros[5]
  print("O quartil3 da lista 1 é", resultado2)
elif len(numeros) == 8:
  resultado2 = numeros[6]
  print("O quartil3 da lista 1 é", resultado2)
elif len(numeros) == 9:
  resultado2 = ((numeros[6] + numeros[7]) / 2)
  print("O quartil3 da lista 1 é", resultado2)
elif len(numeros) == 10:
  resultado2 = ((numeros[7] + numeros[8]) / 2)
  print("O quartil3 da lista 1 é", resultado2)
elif len(numeros) == 11:
  resultado2 = numeros[8]
  print("O quartil3 da lista 1 é", resultado2)
elif len(numeros) == 12:
  resultado2 = numeros[9]
  print("O quartil3 da lista 1 é", resultado2)
elif len(numeros) == 13:
  resultado2 = ((numeros[9] + numeros[10]) / 2)
  print("O quartil3 da lista 1 é", resultado2)
elif len(numeros) == 14:
  resultado2 = ((numeros[10] + numeros[11]) / 2)
  print("O quartil3 da lista 1 é", resultado2)
elif len(numeros) == 15:
  resultado2 = numeros[11]
  print("O quartil3 da lista 1 é", resultado2)
else:
  print("Número maximo de indices excedidos, tente novamente")

#QUARTIL1 DA LISTA2 == resultado3

if len(numeros1) <= 3:
  resultado3 = numeros1[0]
  print("O quartil1 da lista 1 é", resultado3)
elif len(numeros1) == 4:
  resultado3 = ((numeros1[0] + numeros1[1]) / 2)
  print("O quartil1 da lista 1 é", resultado3)
elif len(numeros1) == 5:
  resultado3 = ((numeros1[0] + numeros1[1]) / 2)
  print("O quartil1 da lista 1 é", resultado3)
elif len(numeros1) == 6:
  resultado3 = numeros1[1]
  print("O quartil1 da lista 1 é", resultado3)
elif len(numeros1) == 7:
  resultado3 = numeros1[1]
  print("O quartil1 da lista 1 é", resultado3)
elif len(numeros1) == 8:
  resultado3 = numeros1[1]
  print("O quartil1 da lista 1 é", resultado3)
elif len(numeros1) == 9:
  resultado3 = ((numeros1[1] + numeros1[2]) / 2)
  print("O quartil1 da lista 1 é", resultado3)
elif len(numeros1) == 10:
  resultado3 = ((numeros1[1] + numeros1[2]) / 2 )
  print("O quartil1 da lista 1 é", resultado3)
elif len(numeros1) == 11:
  resultado3 = numeros[2]
  print("O quartil1 da lista 1 é", resultado3)
elif len(numeros1) == 12:
  resultado3 = ((numero1s[2] + numeros1[3]) / 2)
  print("O quartil1 da lista 1 é", resultado3)
elif len(numeros1) == 13:
  resultado3 = ((numeros1[2] + numeros1[3]) / 2)
  print("O quartil1 da lista 1 é", resultado3)
elif len(numeros1) == 14:
  resultado3 = numeros1[3]
  print("O quartil1 da lista 1 é", resultado3)
else:
  print("Número maximo de indices excedidos, tente novamente")

#QUARTIL2 DA LISTA2

if len(numeros1) <= 3:
  resultado4 = numeros1[2]
  print("O quartil3 da lista 1 é", resultado4)
elif len(numeros1) == 4:
  resultado4 =  numeros1[3]
  print("O quartil3 da lista 1 é", resultado4)
elif len(numeros1) == 5:
  resultado4 =  ((numeros1[3] + numeros1[4]) / 2)
  print("O quartil3 da lista 1 é", resultado4)
elif len(numeros1) == 6:
  resultado4 =  ((numeros1[4] + numeros1[5]) / 2)
  print("O quartil3 da lista 1 é", resultado4)
elif len(numeros1) == 7:
  resultado4 = numeros1[5]
  print("O quartil3 da lista 1 é", resultado4)
elif len(numeros1) == 8:
  resultado4 = numeros1[6]
  print("O quartil3 da lista 1 é", resultado4)
elif len(numeros1) == 9:
  resultado4 = ((numeros1[6] + numeros1[7]) / 2)
  print("O quartil3 da lista 1 é", resultado4)
elif len(numeros1) == 10:
  resultado4 = ((numeros1[7] + numeros1[8]) / 2)
  print("O quartil3 da lista 1 é", resultado4)
elif len(numeros1) == 11:
  resultado4 = numeros1[8]
  print("O quartiL3 da lista 1 é", resultado4)
elif len(numeros1) == 12:
  resultado4 = numeros1[9]
  print("O quartil3 da lista 1 é", resultado4)
elif len(numeros1) == 13:
  resultado4 = ((numeros1[9] + numeros1[10]) / 2)
  print("O quartil3 da lista 1 é", resultado4)
elif len(numeros1) == 14:
  resultado4 = ((numeros1[10] + numeros1[11]) / 2)
  print("O quartil3 da lista 1 é", resultado4)
elif len(numeros1) == 15:
  resultado4 = numeros1[11]
  print("O quartil3 da lista 1 é", resultado4)
else:
  print("Número maximo de indices excedidos, tente novamente")
  
#AIQ -> AMPLITUDE INTERQUARTÍLICA

aiql1 = resultado2 - resultado
aiql2 = resultado4 - resultado3

print("A amplitude interquatílica da lista 1 é", aiql1)
print("A amplitude interquatílica da lista 2 é", aiql2)

# LIMITE INFERIOR E SUPERIOR DA LISTA 1

Li_lista1 = resultado - (1.5 * aiql1)
Ls_Lista1 = resultado2 + (1.5 * aiql1)

Li_lista2 = resultado3 - (1.5 * aiql2)
Ls_Lista2 = resultado4 + (1.5 * aiql2)

print("O limite inferior da lista 1 é", Li_lista1)
print("O limite superior da lista 1 é", Ls_Lista1)
print("-------------------------------------")
print("O limite inferior da lista 2 é", Li_lista2)
print("O limite superior da lista 2 é", Ls_Lista2)

#Identificação e classificação de possíveis outliers na amostra
print("Vamos analisar possiveis outliers na amostra apresentada, um momento....")

if mediana_finalista1 > Ls_Lista1 or mediana_finalista1 < Li_lista1:
  print("Identificamos um possivel outlier na lista 1 com relação entre a média e os limites superiores e inferiores do bloxpot")
elif mediana_finalista1 <= Ls_Lista1 and mediana_finalista1 <= Li_lista1:
  print("Não identificamos um possivel outlier na lista 1 com relação entre a média e os limites superiores e inferiores do bloxpot")
elif mediana_finalista2 > Ls_Lista2 or mediana_finalista2 < Li_lista2:
  print("Identificamos um possivel outlier na lista 1 com relação entre a média e os limites superiores e inferiores do bloxpot")
elif mediana_finalista2 <= Ls_Lista2 and mediana_finalista2 <= Li_lista2:
  print("Não identificamos um possivel outlier na lista 1 com relação entre a média e os limites superiores e inferiores do bloxpot")
else:
  print("Nosso código não conseguiu efetuar a analise de outliers com base na amostra anexada, verifique os dados informados e tente novamente")

#Coeficiente de Correlação de Pearson ( r );
x = numeros
y = numeros1
for i in range(len(x)):
  x[i] = float(x[i])
  y[i] = float(y[i])
xquad = []
yquad = []
xy = []
for i in range(len(x)):
  xquad.append(x[i]**2)
  yquad.append(y[i]**2)
  xy.append(x[i]*y[i])
sx = sum(x)
sy = sum(y)
sxquad = sum(xquad)
syquad = sum(yquad)
sxy = sum(xy)
print(f'A soma dos valores de x é {sx}')
print(f'A soma dos valores de y é {sy}')
print(f'A soma dos valores de xquad é {sxquad}')
print(f'A soma dos valores de yquad é {syquad}')
print(f'A soma dos valores de xy é {sxy}')

r_part1 = sxy - ((sx * sy) / len(numeros))
r_part2 = (sxquad - (((sx) ** 2) / len(numeros))) * (syquad - (((sy) ** 2) / len(numeros)))
r_part3 = r_part2 ** 0.5
r_partf = r_part1 / r_part3
print("------------calculos-------------------")
print(r_part1)
print(r_part2)
print(r_part3)
print("---------------------------------------")
print("O coeficiente de Pearson das 2 listas é", r_partf)

#Coeficiente de determinação ( r ao quadrado);
coef_det = r_partf ** 2
print("O coeficiente de determinação das listas é", coef_det)

#Coeficiente b ou Beta da equação de regressão linear simples

b_part1 = sxy - ((sx * sy) / len(numeros))
b_part2 = sxquad - (((sx)**2) / len(numeros))
beta = b_part1 / b_part2
print("-----------Calculos-------------")
print(b_part1)
print(b_part2)
print("--------------------------------")
print("O coeficiente Beta é", beta)

#Coeficiente a ou alpha da equação de regressão linear simples

x_total = sx / len(numeros)
y_total = sy / len(numeros)

alpha = y_total - x_total * beta
print("O coeficiente de Alpha é", alpha)

#Modelo Geral
print("-------------------------------")
propagação = int(input('Informe um número para ser relacionada a lista 1 para que possamos faze uma analise de previsão: '))
previsto = alpha + beta * propagação
print("O nivel esperado de previsão é", previsto)
