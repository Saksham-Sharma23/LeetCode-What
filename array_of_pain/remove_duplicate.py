#BRUTE FORCE - Remove duplicate from sorted array O(n) and SC - O(n)
def remove_duplicates(arr):
    s = set()
    for i in range(len(arr) -1):
        s.add(arr[i])

    return len(s)

arr = [1,2,3,3,5,5,65,67,65]
print(remove_duplicates(arr))


#Optimal