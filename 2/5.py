def PatternMatching(t,p):
    data = []
    for i in range(len(t)-len(p)+1):
        if t[i: i + len(p)] == p:
            data.append(i)
            
    return sorted(data)

pattern = input()
text = input()
print(' '.join(str(x) for x in PatternMatching(text, pattern)))