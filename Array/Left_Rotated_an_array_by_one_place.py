def checkRotation(nums,k):
    n = len(nums)
    k = k % n # Handle cases where k is larger than n
    def reverse(arr,start,end):
        while start < end:
            arr[start], arr[end] = arr[end], arrr[start]
            start += 1
            end -= 1
    reverse(nums,0,n-1) # Reverse the entire array
    reverse(nums,0,k-1) # Reverse the first k elements
    reverse(nums,k,n-1) # Reverse the remaining elements
    return nums