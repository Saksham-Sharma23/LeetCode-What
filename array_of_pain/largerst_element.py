#Brute Force - TC - O(nlogn)
def largest_element(nums):
    if len(nums) == 0:
        return -1
    if len(nums) == 1:
        return nums[0]
    nums.sort()
    return nums[-1]


arr = [1,2,34,4,6,7,8]
# print(largest_element(arr))

#Optimal  - TC - O(n)
def optimal_largest_element(nums):
    if len(nums) == 0:
        return -1
    
    largest = nums[0]

    for i in range(1 , len(nums) - 1 ):
        if nums[i] > largest:
            largest = nums[i]

    return largest


print(optimal_largest_element(arr))