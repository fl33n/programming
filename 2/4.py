import itertools

def ComputingFrequencies(genome, k):
    z = {}
    for n in range(len(genome)-k + 1):
        Pattern = genome[n:n+k]
        if Pattern not in z:
            z[Pattern] = 1
        else:
            z[Pattern] += 1
    return z

def FasterFrequentWords(text, k):
    data = ComputingFrequencies(text, int(k))
    maxpattern = max(data.values())
    result = []
    for i in data:
        if data[i] == maxpattern:
            result.append(i)
    return sorted(result)

text = input()
k = int(input())
print(*FasterFrequentWords(text,k))