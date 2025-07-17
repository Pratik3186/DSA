def LinearSearch(arr):
    nums = int(input("Enter thr number of the emements in the array: "))
    n = len(arr)
    for i in range(0,n):
        if arr[i] == nums:
            return i
    return -1  # Return -1 if the element is not found
arr = [1, 2, 3, 4, 5]
result = LinearSearch(arr)  
print(result)  # Output: Index of the element if found, otherwise -1