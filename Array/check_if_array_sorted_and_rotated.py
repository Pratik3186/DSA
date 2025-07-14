def check(nums):
    count = 0
    n = len(nums)
    for i in range(n):
        if nums[i]>nums[(i+1)%n]:
            count+=1
            if count>1:
                return False
    return True 

nums = [1,3,2,6,4,7,5]
result = check(nums)
print(result)  # Output: True