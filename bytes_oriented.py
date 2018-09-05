# coding utf-8


def bytes_oriented():
    # Define os delimitadores do enquadramento orientado a caracter
    delimiter = 'STX'

    print('Digite uma sequencia de caracteres: ')
    characters = input()

    transmission = bytes_oriented_encode(characters, delimiter, len(characters))

    # print(transmission)
    user_data = bytes_oriented_decode(transmission, len(characters))

    print('Encoded => {}'.format(transmission))
    print('Decoded => {}'.format(user_data))
    print('Message => {}'.format(characters))


def bytes_oriented_encode(characters, delimiter, length):
    transmission = delimiter + str(length) + characters

    return transmission


def bytes_oriented_decode(transmission, length):
    return transmission[-length:]
