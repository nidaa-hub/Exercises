def linear_search(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return True
    return False


arr = [8, 2, 3, 6, 7, 1, 10, 5, 4]
print(linear_search(arr, 5))
print(linear_search(arr, 9))

def binary_search(arr, num):
    first , last = 0 ,len(arr)
    while first <= last:
        mid = (first + last)// 2
        value = arr[mid]
        if value == num:
            return mid
        elif value < num:
            first = mid + 1
        else:
            last = mid - 1
    return -1


arr=[1,2,3,4,5,6,7,8,10]
print(binary_search(arr,5))
print(binary_search(arr,9))