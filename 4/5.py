def h_sort(h, arr):
    for i in range(h, len(arr)):
        j = i
        while j >= h and arr[j] < arr[j - h]:
            arr[j], arr[j - h] = arr[j - h], arr[j]
            j -= h
        print(*arr)
    return arr

h = int(input())
arr = list(map(int, input().split()))
h_sort(h, arr)