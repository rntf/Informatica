## 
#  Questo programma trasforma un intero nella sua descrizione in inglese.
#

def main():
    value = int(input("Please enter a positive integer < 1000: "))
    print(int_name(value))


def int_name(number):
    """
    Trasforma un numero nella sua descrizione inglese a parole.

    :param number: un numero intero positivo < 1000
    :return: la descrizione del numero (e.g. "two hundred seventy four")
    """
    part = number   # La parte che deve ancora essere convertita.
    name = ""   	# Il nome del numero.
    
    if part >= 100:
       name = digit_name(part // 100) + " hundred"
       part = part % 100
       
    if part >= 20:
       name = name + " " + tens_name(part)
       part = part % 10
    elif part >= 10:
       name = name + " " + teen_name(part)
       part = 0
       
    if part > 0:
       name = name + " " + digit_name(part)
       
    return name



def digit_name(digit):
    """
    Trasforma una cifra nella sua descrizione inglese a parole.

    :param digit: un numero intero compreso tra 1 e 9 (estremi inclusi)
    :return: la descrizione a parole della cifra ("one", ..., "nine")
    """

    if digit == 1: return "one"
    if digit == 2: return "two"
    if digit == 3: return "three"
    if digit == 4: return "four"
    if digit == 5: return "five"
    if digit == 6: return "six"
    if digit == 7: return "seven"
    if digit == 8: return "eight"
    if digit == 9: return "nine"
    return ""



def teen_name(number):
    """
    Trasforma un numero 10 - 19 nella sua descrizione inglese a parole.

    :param digit: un numero intero compreso tra 10 e 19 (estremi inclusi)
    :return: la descrizione a parole della cifra ("ten", ..., "nineteen")
    """

    if number == 10: return "ten"
    if number == 11: return "eleven"
    if number == 12: return "twelve"
    if number == 13: return "thirteen"
    if number == 14: return "fourteen"
    if number == 15: return "fifteen"
    if number == 16: return "sixteen"
    if number == 17: return "seventeen"
    if number == 18: return "eighteen"
    if number == 19: return "nineteen"
    return ""



def tens_name(number):
    """
    Fornisce il nome inglese delle decine di un numero tra 20 e 99.

    :param digit: un numero intero compreso tra 20 e 99 (estremi inclusi)
    :return: il nome delle decine del numero ("twenty", ..., "ninety")
    """

    if number >= 90: return "ninety"
    if number >= 80: return "eighty"
    if number >= 70: return "seventy"
    if number >= 60: return "sixty"
    if number >= 50: return "fifty"
    if number >= 40: return "forty"
    if number >= 30: return "thirty"
    if number >= 20: return "twenty"
    return ""



# Inizio del programma.
main()
