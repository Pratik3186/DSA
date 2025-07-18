def maxconsecutivenumber(nums):
    if not nums:
        return None # Handle empty array
    max_count = 0
    count = 1
    for num in nums:
        if num == 0:
            count +=1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count  # Return the maximum count of consecutive zeros
            