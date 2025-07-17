def union_sorted(arr1,arr2): 
    n = len(arr1)
    m = len(arr2)
    i,j = 0
    result = []
    while i< n and j <m:
        while i>0 and i<n and arr1[i] == arr1[i-1]:
            i+=1 
        while j>0 and j<m and arr2[j] == arr2[j-1]:
            j+=1 
        if i>= n and j>= m:
            break 
        
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i+=1 
        elif arr2[j] < arr1[i]:
            result.append(arr2[j])
            j+=1 
        else:   #equal 
            i+=1 
            j+=1 
    while i<n:
        if i == 0 or arr1[i] != arr1[i-1]:
            result.append(arr1[i])
        i+=1 
    while j<m:
        if j == 0 or arr2[j] != arr2[j-1]:
            result.append(arr2[j])
        j+=1 
    return result
        