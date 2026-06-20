# Brute Force 

def second_largest(arr):
    if len(arr) == 0 or len(arr) == 1:
        return -1
    
    largest = arr[0]

    for i in range(1 , len(arr) -1) :
        if arr[i] > largest:
            largest = arr[i]

    for i in range(len(arr)- 2 , 0):
        if arr[i] != largest:
            second = arr[i]
            break


    return arr[i]
        

arr = [1,2,3,54,567,66,7,67,34]

print(second_largest(arr))


def optimal_second_largest(arr):
    largest = arr[0]
    slargest = -1
    
    for i in range(1 , len(arr) - 1):
        if arr[i] > largest:
            slargest = largest
            largest = arr[i]

        elif arr[i] < largest and arr[i] > slargest:
            slargest = arr[i]
    

    return slargest

print(optimal_second_largest(arr))