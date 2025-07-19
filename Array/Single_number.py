def singleNumber(nums):
    """
    This function finds the single number in an array where every other number appears twice.
    
    :param nums: List[int] - List of integers where every element appears twice except for one.
    :return: int - The single number that appears only once.
    """
    result = 0
    for num in nums:
        result ^=num
    return result