def Neighbours(Pattern,d):
    if d == 0:
        return {Pattern}
    if len(Pattern) == 1:
        return {'A', 'C', 'T', 'G'}
    SuffixNeighbors = Neighbours(Pattern[1:], d)
    nucleotides = {'A', 'C', 'T', 'G'}
    result = set()
    for neighbor in SuffixNeighbors:
        if HammingDistance(neighbor, Pattern[1:]) < d:
            for nucleotide in nucleotides:
                result.add(nucleotide + neighbor)
        else:
            result.add(Pattern[0] + neighbor)
    return result


def HammingDistance(a, b):
    return sum(1 for x, y in zip(a, b) if x != y)


pattern = input().strip()
d = int(input().strip())
neighbors = sorted(list(Neighbours(pattern, d)))
print(*neighbors, sep='\n')