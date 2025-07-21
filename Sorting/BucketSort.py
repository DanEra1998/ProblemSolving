def insertionsort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# note that bucket sort depends on the range of value
# this one works for values between 0 - 1 but won't work for
# integers
def bucketsort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]

    for num in arr:
        # represents bucket index
        bi = int(n * num)
        buckets[bi].append(num)

    for b in buckets:
        insertionsort(b)

    index = 0
    for b in buckets:
        for num in b:
            arr[index] = num
            index += 1

arr = [0.1,0.5,0.3,0.9]
bucketsort(arr)
print(arr)
