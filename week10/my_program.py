from week10 import Planet
from week10 import Star
from week10 import PlanetarySystem



sun = Star("Sun")
ss = PlanetarySystem(sun)


p = Planet('mercury', 1, 2, 3)
ss.add_planet(p)

p = Planet('venus', 3, 4, 5)
ss.add_planet(p)

p = Planet('Earth', 5, 6, 7)
ss.add_planet(p)


ss.show_planets