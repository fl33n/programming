def CountNucleotides(dna):
    data = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for letter in dna:
        if letter not in data:
            data[letter] = 0
        data[letter] += 1
    return data


data = CountNucleotides('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
for el in sorted(data.keys()):
    print(data[el], end=' ')