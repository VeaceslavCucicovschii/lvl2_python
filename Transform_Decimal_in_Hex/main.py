from os import system
system('cls')


def FromDecToHex(id):
    counter = 0

    i = len(id) - 1
    while(id[i] != '-'):
        counter += 1
        i -= 1

    dec = int(id[len(id)-counter:])
    Hex = hex(dec)

    return id[:len(id)-counter] + Hex[2:].upper()


id = "2022-01-10-11-01-01-123456"
print(f"Initial: {id}")
print(f"Result:  {FromDecToHex(id)}")
