def findsecondlargest(arr):
    if len(arr) <2:
        return None # Handle arrays with less than 2 elements
    largest = arr[0]
    second_largest = None
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num # Update if found larger
        elif num!= largest and (second_largest is  None or num > second_largest):
            second_largest = num # Update second largest if found larger than current second largest
    return second_largest

arr = [10, 5, 20, 8, 25, 3]
arr = [1,7,7,7,7,7,7,7,7,7]
result = findsecondlargest(arr)
print(result)  # Output: 20