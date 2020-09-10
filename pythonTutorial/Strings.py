x = 'Pluto is a planet'
y = "Pluto is a planet"

print(x == y)
print("Pluto's a planet!")
print('My dog is named "Pluto"')
print('Pluto\'s a planet!')

hello = "hello\nworld"
print(hello)

triplequoted_hello = """hello 
world"""
print(triplequoted_hello)
ToF = triplequoted_hello == hello
print(ToF)

print("hello")
print("world")
print("hello", end='')
print("pluto", end='')
print("------")

# Indexing
planet = 'Pluto'
print(planet[0])
# Slicing
print(planet[-3:])
print(len(planet))

res = [char + '!' for char in planet]
print(res)

# ALL CAPS
claim = "Pluto is a planet!"
print(claim.upper())
print(claim.lower()) # all lowercase
print(claim.index('plan'))  # Searching for the first index of a substring
print(claim.startswith('Pl')) #P,Pl,Plu ...
print(claim.endswith('planet')) # !

words = claim.split()
print(words)

datestr = '1956-01-31'
year, month, day = datestr.split('-')
print(year, month, day)

res = '/'.join([month, day, year])
print(res)

res = ' 👏 '.join([word.upper() for word in words])
print(res)

print(planet + ', we miss you.')

position = 9
res = planet + ", you'll always be the " + str(position) + "th planet to me"
print(res)

res = "{}, you'll always be the {}th planet to me.".format(planet, position)
print(res)

pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390

res = "{} weighs about {:.2} kilogram ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
)
print(res)

# Referring to format() arguments by index, starting from 0
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)

numbers = {'one':1, 'two':2, 'three':3}

print(numbers['one'])

numbers['eleven'] = 11
print(numbers)

numbers['one'] = 'Pluto'
print(numbers)

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial)

print('Saturn' in planet_to_initial) # True
print('Betelgeuse' in planet_to_initial) # False

for k in numbers:
    print("{} = {}".format(k, numbers[k]))
# Get all the initial, sort them alphabetically, and put them in a space-separated string
res = ' '.join(sorted(planet_to_initial.values()))
print(res)

for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))



