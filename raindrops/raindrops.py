def convert(number):
    returnstr = ""

    if number % 3 == 0:
        returnstr = "Pling"

    if number % 5 == 0:
        returnstr += "Plang"

    if number % 7 == 0:
        returnstr += "Plong"

    return returnstr if returnstr else str(number)
