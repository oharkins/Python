orbital_periods = {
    'mercury': 0.2408467,
    'venus': 0.61519726,
    'earth': 1,
    'mars': 1.8808158,
    'jupiter': 11.862615,
    'saturn': 29.447498,
    'uranus': 84.016846,
    'neptune': 164.79132,
}


class SpaceAge(object):

    def __init__(self, seconds):
        self.earth_age = seconds / 31557600

        for planet in orbital_periods:
            age_function = lambda p=planet: round(self.earth_age / orbital_periods[p], 2)
            setattr(self, 'on_' + planet, age_function)
