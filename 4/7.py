def counting_sort(arr):
    count = [0] * 1001
    sorted_arr = [0] * len(arr)
    for num in arr:
        count[num] += 1
    for i in range(1, 1001):
        count[i] += count[i-1]
    for num in arr[::-1]:
        sorted_arr[count[num]-1] = num
        count[num] -= 1
    return ' '.join(map(str, sorted_arr))

nums = input().split()
nums = list(map(int, nums))
print(counting_sort(nums))