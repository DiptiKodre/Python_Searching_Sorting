
# TC = O(n log n)
# SC = O(n)
nums = [2, 4, 3, 8, 9, 6, 1, 5, 7] 

def merge_array(left, right):  
    result = []  # Creates an empty list for the merged values.
    i, j = 0, 0  # Sets pointers for the current elements in left and right.
    n, m = len(left), len(right)  
    while i < n and j < m:  
        if left[i] < right[j]:  
            result.append(left[i]) 
            i += 1  # Moves the left pointer to the next element.
        else:  
            result.append(right[j])  # Adds the smaller right value to the result.
            j += 1  # Moves the right pointer to the next element.

    if i < n:  # Checks whether elements remain in the left list.
        while i < n:  # Adds all remaining left elements.
            result.append(left[i])  # Adds the current left value to the result.
            i += 1  # Moves the left pointer to the next element.
    if j < m:  # Checks whether elements remain in the right list.
        while j < m:  # Adds all remaining right elements.
            result.append(right[j])  # Adds the current right value to the result.
            j += 1  # Moves the right pointer to the next element.
    return result  # Returns the combined sorted list.

def merge_sort(arr):  
    if len(arr) <= 1: 
        return arr  
    mid = len(arr) // 2  
    left_arr = arr[:mid]  
    right_arr = arr[mid:]  
    left = merge_sort(left_arr)  # Recursively sorts the left half.
    right = merge_sort(right_arr)  # Recursively sorts the right half.
    return merge_array(left, right)  # Merges and returns the two sorted halves.

print("Array before sorting : ", nums)  
sorted_array = merge_sort(nums)  
print("Array after sorting : ", sorted_array)  