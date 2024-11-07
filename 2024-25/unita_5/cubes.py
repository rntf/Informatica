##
#  Questo programma calcola i volumi di due cubi.
#

def main():
    result1 = cube_volume(2)
    result2 = cube_volume(10)
    print("A cube with side length 2 has volume", result1)
    print("A cube with side length 10 has volume", result2)


def cube_volume(side_length):
    """
    Calcola il volume di un cubo

    :param side_length: la lunghezza di un lato del cubo
    :return: il volume del cubo
    """
    volume = side_length ** 3
    return volume


# Inizio del programma.
main()
