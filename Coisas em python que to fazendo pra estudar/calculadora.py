#Calculadora Simples

N1 = int(input('Digite seu numero: '))
N2 = int(input('Digite seu segundo numero: '))

print('Selecione o operador: ')
print('1- **Adição**')
print('2- **Subtração**')
print('3- **Multiplicação**')
print('4- **Divisão**')

opçao =input('Selecione entre: 1/2/3/4 ')
if opçao == "1":
    print(f'Seu resultado é: {N1 + N2}')
elif opçao == "2":
    print(f'Seu resultado é: {N1 - N2}')
elif opçao == "3":
    print(f'Seu resultado é: {N1 / N2}')
elif opçao =="4":
    if N2 != 0:
        print(f'Seu resultado é: {N1 / N2}')
    else:
        print('Erro: Divisão por zero!!')
else:
    print("Opção invalida!")
2