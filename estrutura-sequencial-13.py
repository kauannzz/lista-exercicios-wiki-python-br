print('Olá, eu me chamo Logan, sou uma IA criada pra saber seu peso ideal. Antes de tudo, preciso saber...')

selecao = int(input('Você é homem ou mulher? Digite (1) para homem ou (2) para mulher: '))

if(selecao == 1):
    altura_h = float(input('Digite sua altura: '))
    homem_ideal = (72.7*altura_h) - 58 #Algoritimo que calcula o peso ideal masculino
    print('Seu peso ideal é:', homem_ideal.__round__(2))    #Deixando apenas duas casas decimais após o número inteiro
elif(selecao == 2):
    altura_f = float(input('Digite sua altura: '))
    mulher_ideal = (62.1*altura_f) - 44.7#Algorito que calcula o peso ideal feminino
    print('Seu peso ideal é:', mulher_ideal.__round__(2))   #Deixando apenas duas casas decimais após o número inteiro
else:
    print('Dados inválidos')