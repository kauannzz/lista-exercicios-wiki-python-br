from time import sleep

valor_hora = float(input('Quanto você ganha por hora: '))
numero_mes = float(input('Quantas horas você trabalha por mês: '))

salario = valor_hora * numero_mes #Calculo pra saber qual o valor do salário bruto

print('Salário bruto:', salario)
print('Calculando o que você terá que pagar ao governo... ')
sleep(2)

imposto_renda = salario * 0.11 #Porcentagem de 11%
print('Imposto de Renda (11%): R$', imposto_renda.__round__(2))

inss = salario * 0.08 #Porcentagem de 8%
print('INSS: (8%) R$:', inss.__round__(2))

sindicato = salario * 0.05 #Porcentagem de 5%
print('SINDICATO (5%) R$', sindicato.__round__(2))

salario_liquido = salario - imposto_renda - inss - sindicato #Salário liquido
print('Salário liquido: R$', salario_liquido.__round__(2))
