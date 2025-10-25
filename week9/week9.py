import math
class Planet:
    def __init__(self, _name, _radius, _mass, _distance):
        self.name = _name
        self.radius = _radius
        self.mass = _mass
        self.distance = _distance

    def get_name(self):
        return self.name
    
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_distance(self):
        return self.distance
    
    def get_volume(self):
        volume = 4/3 * math.pi * self.radius ** 3
        return volume
    
    def get_density(self):
        density = self.mass / self.get_volume()
        return density
    
    def set_name(self, new_name):
        self.name = new_name

    def __str__(self):
        msg = ''
        msg += f'hello {self.get_name()}. How are you?'
        return msg

    

planet1 = Planet('x25', 45, 198, 1000)
planet2 = Planet("z37", 12, 234, 2381)

print(planet1)

