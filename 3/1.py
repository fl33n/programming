def MinSkew(genome):
    skew = [0]
    for i in range(1, len(genome) + 1):
        if genome[i - 1] == 'G':
            skew.append(skew[i - 1] + 1)
        elif genome[i - 1] == 'C':
            skew.append(skew[i - 1] - 1)
        else:
            skew.append(skew[i - 1])

    min_val = min(skew)

    return [i for i, val in enumerate(skew) if val == min_val]

print(*MinSkew(input()))