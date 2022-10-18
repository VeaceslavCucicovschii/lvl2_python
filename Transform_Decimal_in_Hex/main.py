from http.client import SWITCHING_PROTOCOLS
from os import system
system('cls')


def FromDecToHex(id):
    counter = 0
    result = ''

    i = len(id) - 1
    while(id[i] != '-'):
        counter += 1
        i -= 1

    dec = int(id[len(id)-counter:])

    while(dec != 0):
        match dec % 16:
            case 10:
                result += 'A'
            case 11:
                result += 'B'
            case 12:
                result += 'C'
            case 13:
                result += 'D'
            case 14:
                result += 'E'
            case 15:
                result += 'F'
            case default:
                result += str(dec % 16)
        dec //= 16

    result = result[::-1]
    return f'{id[:len(id)-counter]}{result}'


id = "2022-01-10-11-01-01-123456"
print(f"Initial: {id}")
print(f"Result:  {FromDecToHex(id)}")
