def possible_expressions(nums, current_sum=0, expression=""):
    if not nums:
        return [(expression, current_sum)]

    result_plus = possible_expressions(nums[1:], current_sum+nums[0], f"{expression}+{nums[0]}")
    result_minus = possible_expressions(nums[1:], current_sum-nums[0], f"{expression}-{nums[0]}")
    return result_plus + result_minus

nums = [int(el) for el in input().split(", ")]
print(*[f"{el[0]}={el[1]}" for el in possible_expressions(nums)], sep="\n")