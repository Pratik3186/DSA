def majority_element(nums):
    """
    Find the majority element in an array.
    The majority element is the element that appears more than n/2 times.
    
    :param nums: List[int] - List of integers
    :return: int - The majority element
    """
    count = 0
    candidate = None
    
    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1
    
    return candidate