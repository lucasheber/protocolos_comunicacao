# coding utf-8

import bitabit
import character_oriented
import bytes_oriented


def menu():
    opcoes = {
        '1': bitabit.bitabit,
        '2': character_oriented.character_oriented,
        '3': bytes_oriented.bytes_oriented
    }

    print('1. Bit a Bit')
    print('2. Orientado a caracter')
    print('3. Orientado a bytes')
    opcao = input('Escolha uma opcao: ')

    try:

        opcoes[opcao]()

    except KeyError:
        print("\nA opcao passada não é válida!\nO programa será finalizado.")


def main():
    menu()


if __name__ == '__main__':
    main()
