print('Seja bem vindo(a). \nEsse é um Programa para Exercitar os !!SEUS!! calculos voltado a REDES DE COMPUTADORES')
print('*' * 80)
while True:
    op_1 = int(input('O que você deseja fazer? '
                     '\n[ 1 ] Converter um Decimal para Binário.'
                     '\n[ 2 ] Converter um Decimal para Hexadecimal.'
                     '\n[ 3 ] Sortear um numero aleatoria para VOCÊ converter par Binário & Hexdecimal.'
                     '\n>>>SUA opção: '))
    print('*' * 80)

    if op_1 > 3:
        print('Essa opção não existe!!')
        break

    if op_1 == 1:
        while True:
            print('VOCÊ ESCOLHEU CONVERTER UM NUMERO DECIMAL PARA BINÁRIO!!!')
            num = int(input('\nDigite um numero em DECIMAL para ser convertido para BINÁRIO: '))
            print(f'O numero {num} em BINÁRIO fica {bin(num)[2:]}')

            op_2 = str(input('Você desja continuar a gerar mais numeros BINÁRIOS? [S/N] ')).strip().upper()[0:]
            if op_2 == 'S':
                continue
            else:
                print('*' * 80)
                break

    if op_1 == 2:
        while True:
            print('VOCÊ ESCOLHEU CONVERTER UM NUMERO DECIMAL PARA HEXADECIMAL!!!')
            num = int(input('\nDigite um numero em DECIMAL para ser convertido para HEXADECIMAL: '))
            print(f'O numero {num} em HEXADECIMAL fica {hex(num)[2:]}')

            op_2 = str(input('Você desja continuar a gerar mais numeros HEXADECIMAL? [S/N] ')).strip().upper()[0:]
            if op_2 == 'S':
                continue
            else:
                print('*' * 80)
                break

    if op_1 == 3:
        while True:
            from  random import randint
            print('VOCÊ ESCOLHEU SORTEAR UM NUMERO ALEATORIO PARA \033[31mVOCÊ MESMO CONVERTER\033[m')
            print(f'O numero gerado foi: \033[31m{randint(0, 999999)}\033[m')

            op_2 = str(input('Você desja continuar a SORTEAR mais algum numero? [S/N] ')).strip().upper()[0:]
            if op_2 == 'S':
                if op_2 == 'SN':
                    continue

            else:
                print('*' * 80)
                break


print('fim')
