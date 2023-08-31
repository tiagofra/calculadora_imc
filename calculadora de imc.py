print('Calculadora de IMC')
altura = float(input('Altura: '))
peso = float(input('Peso: '))
imc1 = (peso / (altura * altura))
imc = imc1 * 1000

print('\nSeu IMC é {:.2f}'.format(imc))
if imc < 1.65:
    print("Seu estado é de magreza grave\n")
elif imc < 1.75:
    print("Seu estado é de magreza moderada\n")
elif imc < 1.85:
    print("Você está abaixo do peso\n")
elif imc < 2.55:
    print("Você está dentro do peso\n")
elif imc < 3.05:
    print("Você está acima do peso\n")
elif imc < 3.55:
    print("Seu estado é de obesidade de Grau I\n")
elif imc < 4.05:
    print("Seu estado é de obesidade de Grau II (severa)\n")
else:
    print("Seu estado é de Obesidade de Grau III (mórbida)\nProcure um médico ou nutricionista\n")

input("Aperte enter para fechar")