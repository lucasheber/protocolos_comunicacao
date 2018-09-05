# coding utf-8

delimiter = 'DLE'


def character_oriented():
    # Define os delimitadores do enquadramento orientado a caracter
    initial_delimiter = 'STX'
    final_delimiter = 'ETX'

    print('Digite uma sequencia de caracteres: ')
    characters = input()

    transmission = character_oriented_encode(characters, initial_delimiter, final_delimiter)

    # print(transmission)
    user_data = character_oriented_decode(transmission, initial_delimiter, final_delimiter)

    print('Encoded => {}'.format(transmission))
    print('Decoded => {}'.format(user_data))
    print('Message => {}'.format(characters))


def character_oriented_encode(characters, initial_delimiter, final_delimiter):

    transmission = characters.replace(delimiter, delimiter + delimiter)
    transmission = transmission.replace(initial_delimiter, delimiter + initial_delimiter)
    transmission = transmission.replace(final_delimiter, delimiter + final_delimiter)

    transmission = initial_delimiter + transmission + final_delimiter

    return transmission


def character_oriented_decode(transmission, initial_delimiter, final_delimiter):

    user_data = transmission.replace(delimiter + delimiter, delimiter)
    user_data = user_data.replace(delimiter + initial_delimiter, initial_delimiter)
    user_data = user_data.replace(delimiter + final_delimiter, final_delimiter)

    user_data = user_data[len(initial_delimiter):]
    user_data = user_data[:-len(final_delimiter)]

    return user_data
