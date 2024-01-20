def bubblesort(arr):
    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)-i-1):
          if arr[j] > arr[j+1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr=[8,2,3,6,7,1,10,5,4]
print("Sorted Array:",bubblesort(arr))


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


arr = [8, 7, 3, 1, 6, 12, 17, 5, 9, 20, 1]
merge_sort(arr)
print("Sorted Array:", arr)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left ,middle ,right = [] ,[] ,[]
    for i in arr:
        if i < pivot:
            left.append(i)
        elif i == pivot:
            middle.append(i)
        elif i > pivot:
            right.append(i)
    return quicksort(left) + middle + quicksort(right)

arr = [8,2,3,6,7,1,10,5,4,9,20,78,0]
print("Sorted Array:", quicksort(arr))