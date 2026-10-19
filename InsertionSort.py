#TC = O(n^2)-->avg/worst case and O(n)--> best case(sorted array)
#SC = O(1)

nums = [3,5,6,4,8,9,10,7,1]

print("Array before sorting : ",nums)
n = len(nums)
for i in range(1,n):  #Starts from the second element, because the first element is already considered sorted.
    key = nums[i]    #Stores the current element in key 
    j = i-1                 #sets j to the previous index.
    while j>=0 and nums[j]> key:          #j >= 0 Checks that j is a valid list index.List indexes start at 0, so the loop must stop when j becomes -1.
                                          #nums[j] > key Checks whether the element at index j is greater than key. If it is greater, 
                                          # that element must move one position to the right to make space for key.
        nums[j+1] = nums[j]      #Moves larger preceding elements one position to the right.
        j -= 1
    nums[j+1] = key       #Places key into the gap created by shifting the larger elements.

print("Array after sorting : ",nums)