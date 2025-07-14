def check(arr):
    if not arr:
        return None # Handle empty array
    left = 0
    for right in range(1,(arr-1)):
        if arr[right] != arr[left]:    
            left +=1 
            arr[left] = arr[right]
    return left + 1  # Return the length of the array without duplicates
