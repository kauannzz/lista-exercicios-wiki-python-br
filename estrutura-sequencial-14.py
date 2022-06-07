
peso_peixes = float(input('Digite o peso do peixe: '))

if(peso_peixes > 50):
    #Lógica pra calcular o valor do excesso do peso do peixe e o valor da multa
    excesso = peso_peixes - 50
    multa = excesso * 4

    print('O Peso do peixe excede {} o peso estabelecido pelo regulamento, portando sua multa será de R${}'.format(excesso, multa))

else:
    print('O peso não excede o peso estabelecido. Não terá multa nenhuma :)')
