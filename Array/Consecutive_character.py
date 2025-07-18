def consecutive_character(s):
    if not s:
        return None # Handle empty string
    max_count = 1
    count = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 1
    return max_count  # Return the maximum count of consecutive characters