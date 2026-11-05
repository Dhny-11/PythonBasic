class Planet:
    def __init__(self,name, planet_type, star):
        if not isinstance(name, str) or not isinstance(planet_type, str) or not isinstance(star, str):
            raise TypeError('name, planet type, and star must be strings')
        if not name or not planet_type or not star:
            raise ValueError('name , planet_type, and star must be non-empty strings')
        self.name = name
        self.planet_type = planet_type 
        self.star = star
    
    def orbit(self):
        return f'{self.name} is orbiting around {self.star}...'

    def __str__(self):
        return f'Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}'
        
planet1 = Planet('Earth', 'Terrestrial', 'Sun')
planet2 = Planet('Jupiter', 'Gas Giant', 'Sun')
planet3 = Planet('Kepler-22b', 'Exoplanet', 'Kepler-22')

print(planet1)
print(planet2)
print(planet3)