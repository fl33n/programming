def FrequentWords(text, k):
    if k > len(text):
        return None
    if k == len(text):
        return {text:1}
    list_substr = list()
    for j in range(len(text) - k + 1):
        list_substr.append( text[j:j+k])
    res = dict()
    for j in range(len(list_substr)):
        key_val = list_substr[j]
        res[key_val] = res.get(key_val, 0) + 1

    return res

text = input()
k = int(input())
d = FrequentWords(text, k)
max_value = max(d.values())
for key in sorted(d):
    if d[key] == max_value:
        print(key, end=' ')