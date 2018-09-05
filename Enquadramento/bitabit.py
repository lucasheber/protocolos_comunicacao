# coding utf-8


def bitabit():
    # Define o flag do enquadramento bit a bit
    flag = '01111110'

    print('Digite uma sequencia de bits aleatorios: ')
    caracters = input()

    transmission = biabit_encode(caracters, flag)
    user_data = bitabit_decode(transmission, flag)

    print('Encoded => {}'.format(transmission))
    print('Decoded => {}'.format(user_data))
    print('Message => {}'.format(caracters))


def biabit_encode(message, flag):
    # Armazena a mensagem com o flag e o BitStuffing
    transmission = flag

    # Indica a quantide de um (1) que estao em sequencia
    seq_one = 0

    for caracter in message:

        # BitStuffing
        if seq_one == 5:
            transmission += '0'
            seq_one = 0

        if caracter == '1':
            seq_one += 1
        else:
            seq_one = 0

        transmission += caracter

    transmission += flag

    return transmission


def bitabit_decode(transmission, flag):
    # Indica a quantide de um (1) que estao em sequencia
    seq_one = 0

    # Remove o flag
    transmission = transmission.replace(flag, '')

    # Mensagem decodificada
    user_data = ''

    for caracter in transmission:

        # BitStuffing
        if seq_one != 5:
            user_data += caracter

        if caracter == '1':
            seq_one += 1
        else:
            seq_one = 0

    return user_data

