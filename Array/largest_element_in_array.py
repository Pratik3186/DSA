def findLargest(arr):
    if not arr:
        return None  # Handle empty array

    largest = arr[0]  # Assume first is largest

    for num in arr:
        if num > largest:
            largest = num  # Update if found larger

    return largest

# arr = [10,5,20,8,25,3]
# result = findLargest(arr)
# print(result)
findLargest([10, 5, 20, 8, 25, 3])  # Example usage
# Output: 25