import itertools

text = input()
k = int(input())

def Count(t, p):
    c = 0
    for i in range(len(t)-len(p) + 1):
        if t[i:i+len(p)] == p:
            c += 1
    return c

def ComputingFrequencies(genome, k):
    data = {}
    for i in itertools.product("ACGT", repeat = k):
        data[i] = Count(genome, "".join(i))
    return [i for i in data.values()]


print(*ComputingFrequencies(text, k))