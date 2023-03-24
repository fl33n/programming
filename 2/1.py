def PatternToNumber(dna):
    data = {'A': '0',  'C': '1', 'G': '2', 'T': '3'}
    pre_result = ''
    for el in dna:
        pre_result += data[el]
    
    return int(pre_result, 4)

dna = input()
print(PatternToNumber(dna))