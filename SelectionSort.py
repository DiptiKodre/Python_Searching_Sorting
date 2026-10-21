#TC = O(n^2)
# SC = O(1)

nums = [12, 33, 24, 76, 32, 11, 23, 43, 12]  
def selection_sort(nums):  
    n = len(nums)  
    for i in range(0, n):  # Visits each position where the next smallest value should go.
        min_idx = i  # Assumes the first unsorted element is the smallest.
        for j in range(i + 1, n):  # Checks the remaining unsorted elements.
            if nums[j] < nums[min_idx]:  # Tests whether the current element is smaller.
                min_idx = j  # Stores the index of the new smallest element.

        nums[i], nums[min_idx] = nums[min_idx], nums[i]  # Swaps the smallest value into position i.


print("Before sorting:", nums)  
selection_sort(nums) 
print("After sorting:", nums)  
