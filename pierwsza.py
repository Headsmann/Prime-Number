


def pierwsza(x):
    if x < 2:
        return False
    else:
        if x == 2:
            return True
        else:
            for i in range(2, x):
                if x % i == 0:
                    return False
            return True
def main():
 x = int(raw_input("Wpisz liczbe do sprawdzenia: \n"))
 print pierwsza(x)


main()