
def insertionSort(arr):

    for i in range(1, len(arr)):

        key = arr[i]

        k = i-1
        while k >=0 and key < arr[k] :
                arr[k+1] = arr[k]
                k -= 1
        arr[k+1] = key

arr = [14, 12, 15, 4, 6]
insertionSort(arr)
print(arr)