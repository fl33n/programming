def counting_sort(arr, exp):
    n = len(arr)
    count = [0]*10
    output = [0]*n

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i-1]

    i = n-1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]


def radix_sort(i, arr):
    exp = 1
    for j in range(i):
        exp *= 10

    counting_sort(arr, exp)

    for i in range(len(arr)):
        arr[i] = str(arr[i])

    return ' '.join(arr)


i = int(input())
arr = list(map(int, input().split()))
print(radix_sort(i, arr))
