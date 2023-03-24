def ReverseComplement(dna):
    result = ''
    for el in dna[::-1]:
        result += 'A' if el == 'T' else \
                    'C' if el == 'G' else \
                    'G' if el == 'C' else 'T'
    return result

print(ReverseComplement('AAAACCCGGT'))