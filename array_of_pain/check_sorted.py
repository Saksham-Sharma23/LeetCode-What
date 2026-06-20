def is_sorted(arr):
    for i in range(1 , len(arr) - 1):
        if arr[i] < arr[i-1]:
            return False
    return True

arr = [1,2,3,4,5,6]
arr2 =[2,4,2,4,3,6,21]
arr3 = [5,4,3,2,1]

print(is_sorted(arr))
print(is_sorted(arr2))
print(is_sorted(arr3))