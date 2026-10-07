def add_numbers(nums):
    sum = 0
    for i in range(len(nums) - 1):
        sum += nums[i]
        print("iteration ", i)


def add_numbers_unroll(nums):
    sum = 0
    for i in range((len(nums) - 1) / 2):
        sum += nums[i] + nums[i + 1]
        print("iteration ", i)


lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
add_numbers(lst)
print("unroll")
add_numbers_unroll(lst)
