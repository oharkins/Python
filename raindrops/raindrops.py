def convert(number):
    returnstr = ""
    factor = False
    if number%3 == 0:
        returnstr = "Pling"
        factor = True
    if number%5 == 0:
        returnstr += "Plang"
        factor = True
    if number%7 == 0:
        returnstr += "Plong"
        factor = True
    if not factor:
        return str(number)
    return returnstr


# print(convert(52))
