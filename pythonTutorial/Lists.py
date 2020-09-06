primes = [2, 3, 5, 7]

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'jupiter', 'Saturn', 'Uranus', 'Neptune']

hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'],
]

hands = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]

my_favorite_things = [26, 'League of legend', help]

print(planets[0])
print(planets[1])
print(planets[-1])
print(planets[-2])
print("-------------------------")
print(planets[0:3])
print(planets[:3])
print(planets[3:])
print(planets[1:-1])
print(planets[-3:])

planets[3] = 'Malacandra'
print(planets)
print("----------------------------------------")
planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)
planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars']
print(planets)

length = len(planets)
print(length)

sort = sorted(planets)
print(sort)

primes = [2, 3, 4, 5]
print("sum!!! : ", sum(primes))

print(max(primes))

planets.append('Pluto')
print(planets)

planets.pop()
print(planets)

print(planets.index('Earth'))
print("Earth" in planets)

t = (1, 2, 3)
print(t)

a = 1
b = 0
a, b = b, a
print(a, b)







