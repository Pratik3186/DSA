def checkarray(arr):
    if not arr:
        return None # Handle empty array
    for num in arr:
        if arr[num]<= arr[num+1]:
            continue # Continue if current element is less than or equal to next
        else:
            return False # Return False if any element is greater than next
    return True # Return True if all elements are in sorted order

arr = [1,2,2,3,3,4,5]
# arr = [1,2,1,3,4,5]
result = checkarray(arr)
print(result)  # Output: True

