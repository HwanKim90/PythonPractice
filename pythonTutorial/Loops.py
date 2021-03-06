planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

for planet in planets:
    print(planet, end=' ') # print all on same line

multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult

print(product)

s = 'steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video.'
msg = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end = '')
print("-----------------------------------------")

for i in range(5):
    print("Doing important work. i =", i)

i = 0
while i < 10:
    print(i, end= ' ')
    i += 1

print("------------------------------------------")

squares = [n**2 for n in range(10)]
print(squares)

squares = []
for n in range(10):
    squares.append(n**2)

print(squares)

short_planets = [planet for planet in planets if len(planet) < 6]
print(short_planets)

loud_short_planets = [
                        planet.upper() + '!'
                        for planet in planets
                        if len(planet) < 6
                        ]
print(loud_short_planets)

def count_negatives(nums):
    """Return the number of negative numbers in the given list.

    >>> count_negatives([5, -1, -2, 0, 3])
    2
    """
    # n_negative = 0
    # for num in nums:
    #     if num < 0:
    #         n_negative += 1
    # return n_negative

    # return len([num for num in nums if num < 0])

    return sum([num < 0 for num in nums])
numbers = [-3, -2 ,-1 , 1 ,2 ,3]

print(count_negatives(numbers))


def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is
    True if L[i] is greater than thresh, and False otherwise.

    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    pass
    list = []
    # for l in L:
    #     if l > thresh:
    #         list.append(True)
    #     else:
    #         list.append(False)
    #
    # return list
    for l in L:
        list.append(l > thresh)
    return list

list = [1, 2 ,3 ,4]

result = elementwise_greater_than(list, 2)
print(result)


