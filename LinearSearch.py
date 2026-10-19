#TC = O(N)
#SC = O(1)
nums = [12,45,67,89,90,100]
target = 67
n = len(nums)

for i in range(0,n):
    if nums[i]== target:
        print("Element found at index:",i)
        break
else:
    print("Element not found in the array")