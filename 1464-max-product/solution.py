def maxProduct(nums):
    if len(nums) > 2:
        nums.sort(reverse=True)
    return (nums[0] - 1) * (nums[1] - 1)


print(maxProduct([3, 7]))
