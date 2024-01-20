def reversestring(input_str):
    new_str = ""
    for s in input_str:
        new_str = s + new_str
    return new_str


print("The new string is =", reversestring("abcdefg"))


def max_min_elemant(arr):
    max, min = arr[0], arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]
    return max, min


arr = [1, 2, 3, 4, 5]
print("the maximum and minimum elements in an array is:", max_min_elemant(arr))

def remove_duplicates(arr):
    i = 0
    while i < len(arr) - 1:
        if arr[i] == arr[i + 1]:
            arr.pop(i + 1)
        else:
            i += 1
    return arr

arr=[5,6,8,12,23,56,89,89,89,90,90,95,97,100]
print(remove_duplicates(arr))
