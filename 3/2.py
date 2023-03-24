from functools import reduce

def HammingDistance(s1, s2):
    return reduce(lambda x, y: x + (y[0] != y[1]), zip(s1, s2), 0)

print(HammingDistance(input(), input()))