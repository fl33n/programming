def h_sort(h, arr):
    for i in range(h, len(arr)):
        j = i
        while j >= h and arr[j] < arr[j - h]:
            arr[j], arr[j - h] = arr[j - h], arr[j]
            j -= h
    return arr

def shell_sort(h_sequence, arr):
    for h in h_sequence:
        arr = h_sort(h, arr)
        print(' '.join(map(str, arr)))

h_sequence = list(map(int, input().split()))
arr = list(map(int, input().split()))

shell_sort(h_sequence, arr)