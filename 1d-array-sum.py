def running_sum(nums):
    sum_arr = []
    sum_val = 0
    for num in nums:
        sum_val += num
        sum_arr.append(sum_val)
    return sum_arr


def running_sum_optimized(nums):
    sum_val = 0
    for i in range(len(nums)):
        sum_val += nums[i]
        nums[i] = sum_val
    return nums


nums = [1, 2, 3, 4]
print("Length:", len(nums))

output = running_sum(nums)
print("Output:", output)

output_opt = running_sum_optimized(nums)
print("Output Optimized:", output_opt)
