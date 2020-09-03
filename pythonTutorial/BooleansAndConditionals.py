x = True
print(x)
print(type(x))

def can_run_for_president(age, is_natural_born_citizen):
    """Can someone of the given age run for president in the Korea Republic"""
    # The Korea Republic Constitution says you must be at least 40 years old
    return is_natural_born_citizen and (age >= 40)

# print("Can a 19-year-old run for president?", can_run_for_president(19))
# print("Can a 45-year-old run for president?", can_run_for_president(45))

print(can_run_for_president(19, True))
print(can_run_for_president(55, False))
print(can_run_for_president(55, True))

def is_odd(n):
    return (n % 2) == 1

print("Is 100 odd?", is_odd(100))
print("Is -1 odd?", is_odd(-1))

print(True or True and False)