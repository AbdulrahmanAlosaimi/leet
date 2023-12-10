def minCapability(nums, k):
    cap = float("inf")
    if len(nums) < 3:
        for i in range(len(nums)):
            cap = min(cap, nums[i])
    else:
        for i in range(len(nums)):
            counter = 0
            start = i + 2
            for j, val in enumerate(nums[start:], start=start):
                #            if counter == k:
                #                break
                print("i: ", i, "\t", nums[i], "\nj: ", j, "\t", nums[j], "\n")
                cap = min(cap, max(nums[i], nums[j]))
                counter += 1

    return cap


print(minCapability([2, 2], 1))
