def FrequentWordsWithMismatches(Text, k, d):
    def Neighbors(Pattern, d):
        if d == 0:
            return {Pattern}
        if len(Pattern) == 1:
            return {'A', 'C', 'G', 'T'}
        Neighborhood = set()
        SuffixNeighbors = Neighbors(Pattern[1:], d)
        for Text in SuffixNeighbors:
            if HammingDistance(Pattern[1:], Text) < d:
                for nuc in {'A', 'C', 'G', 'T'}:
                    Neighborhood.add(nuc + Text)
            else:
                Neighborhood.add(Pattern[0] + Text)
        return Neighborhood
    
    def PatternToNumber(pattern):
        if not pattern:
            return 0
        symbol_dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        symbol = pattern[-1]
        prefix = pattern[:-1]
        return 4 * PatternToNumber(prefix) + symbol_dict[symbol]
    
    def NumberToPattern(index, k):
        number_dict = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
        if k == 1:
            return number_dict[index]
        prefix_index = index // 4
        r = index % 4
        symbol = number_dict[r]
        prefix_pattern = NumberToPattern(prefix_index, k-1)
        return prefix_pattern + symbol
    
    def HammingDistance(p, q):
        return sum([1 for i in range(len(p)) if p[i] != q[i]])
    
    n = len(Text)
    freq_array = [0] * (4**k)
    for i in range(n-k+1):
        pattern = Text[i:i+k]
        neighborhood = Neighbors(pattern, d)
        for neighbor in neighborhood:
            index = PatternToNumber(neighbor)
            freq_array[index] += 1
    max_count = max(freq_array)
    sorted_index = sorted([i for i in range(4**k) if freq_array[i] == max_count])
    max_patterns = []
    for ind in sorted_index:
        pattern = NumberToPattern(ind, k)
        max_patterns.append(pattern)
    return max_patterns

Text = input().strip()
k, d = map(int, input().strip().split())
print(*FrequentWordsWithMismatches(Text, k, d))