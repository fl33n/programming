from functools import reduce

def NumberToPattern(index, k):
    data = {'0':'A', '1':'C', '2':'G', '3':'T'}
    new_str = ''
    while index > 0:
        new_str = str(index % 4) + new_str
        index = index // 4       
    new_str = new_str.zfill(k)
    return "".join([data[x] for x in new_str])

def HammingDistance(s1, s2):
    return reduce(lambda x,i: x + (1 if i[0] != i[1] else 0), zip(s1, s2), 0)

def ReverseComplement(dna):
    a = dna[::-1]
    newstr = ""
    for x in a:
        if x == "A":
            newstr += "T"
        elif x == "T":
            newstr += "A"
        elif x == "G":
            newstr += "C"
        elif x == "C":
            newstr += "G"   
    return newstr

def ApproximateFrequentWords(text, k, d):
    counters = [('',0)] * (4**k)
    for i in range(4**k):
        counters[i] = [NumberToPattern(i,k), 0]
    for i in range(len(text) - k + 1):
        substr = text[i:i + k]
        inv_substr = ReverseComplement(substr)
        for x in counters:
            if HammingDistance(substr, x[0]) <= d:
                x[1] += 1
            if HammingDistance(inv_substr, x[0]) <= d:
                x[1] += 1
     
    max_val = (max(counters, key = lambda item: item[1]))[1]
    return map(lambda x: x[0], list(filter(lambda x: x[1] == max_val, counters)))

print(*ApproximateFrequentWords(input(),*list(map(int,input().split()))))