''' Программа ищет два числа из массива которые в сумме дадут n число или максимально близкое к нему. '''


import random

mas = [random.randint(-10000, 100000) for _ in range(800)]
mas = [-5, 20, 15, 1, 1, -10, 2, 3, 4, 5, 30, 6, 7, 8, 9]


def twosum(mas: list[int], n: int) -> list[int]:
    mas.sort()
    l, r = 0, len(mas)-1
    while True:
        temp = mas[l] + mas[r]
        if temp == n:
            return [mas[l], mas[r]]
        if r - l == 1:
            return [mas[l], mas[r]]
        if temp < n:
            l += 1
        else:
            r -= 1


result = twosum(mas, -100)
print(sum(result), result)


def twosum1(nums: list[int], target: int) -> list[int]:
    nums_copy = sorted(nums)
    l, r = 0, len(nums)-1
    while True:
        temp = nums_copy[l] + nums_copy[r]
        if temp == target:
            if nums.index(nums_copy[l]) == nums.index(nums_copy[r]):
                return [nums.index(nums_copy[l]), nums.index(nums_copy[r], r)]
            return [nums.index(nums_copy[l]), nums.index(nums_copy[r])]
        if r - l == 1:
            return [nums.index(nums_copy[l]), nums.index(nums_copy[r])]
        if temp < target:
            l += 1
        else:
            r -= 1


print(twosum1([3, 3], 6))


def twosum2(nums: list[int], target: int) -> list[int]:
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i


print(twosum2([2, 7, 11, 15], 9))
