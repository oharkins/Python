def value(colors):

    value = ""
    for color in colors:
        value += str(colorList().index(color))
    return int(value[:2])


def colorList():
    colorList = [
        'black',
        'brown',
        'red',
        'orange',
        'yellow',
        'green',
        'blue',
        'violet',
        'grey',
        'white'
    ]
    return colorList
