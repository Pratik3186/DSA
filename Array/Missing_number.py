def missingNumber(nums):
    n = len(nums)
    total_sum = n*(n+1)//2
    actual_sum = sum(nums)
    return total_sum - actual_sum  # Return the missing number
# Example usage
# nums = [3, 0, 1]  
# result = missingNumber(nums)
# print(result)  # Output: 2
missingNumber([3, 0, 1])  # Example usage
# Output: 2

#brute force
def missingNumber(nums):
    n = len(nums)
    for i in range(n + 1):
        if i not in nums:
            return i  # Return the missing number