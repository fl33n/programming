def NumberToPattern(index, k):
    b = ''
    while index > 0:
        b = str(index % 4) + b
        index = index // 4
    z = {'0': 'A', '1': 'C', '2': 'G', '3': 'T'}
    return ''.join([z[s] for s in b.zfill(k)])

index, k = map(int, input().split())
print(NumberToPattern(index, k))