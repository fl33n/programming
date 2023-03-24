def FrequentWordsWithSorting(text, k):

    def PatternToNumber(pattern):
        nucleotideDict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        number = 0
        for i in range(k):
            number += nucleotideDict[pattern[i]] * (4 ** (k - i - 1))
        return number

   
    patterns = []
    for i in range(len(text) - k + 1):
        patterns.append(text[i:i+k])


    numbers = []
    for pattern in patterns:
        numbers.append(PatternToNumber(pattern))
    sortedIndex = sorted(range(len(numbers)), key=lambda k: numbers[k])


    count = [1] * len(numbers)
    maxCount = 0
    for i in range(1, len(sortedIndex)):
        if numbers[sortedIndex[i]] == numbers[sortedIndex[i-1]]:
            count[i] = count[i-1] + 1
            maxCount = max(maxCount, count[i])
        else:
            count[i] = 1

 
    frequentPatterns = []
    for i in range(len(sortedIndex)):
        if count[i] == maxCount:
            frequentPatterns.append(sortedIndex[i])

    resultCount = ' '.join(str(x) for x in count)
    resultPatterns = [text[index:index+k] for index in frequentPatterns]
    resultPatterns.sort()

    return resultCount + '\n' + ' '.join(resultPatterns)
text = input()
k = int(input())
print(FrequentWordsWithSorting(text, k))