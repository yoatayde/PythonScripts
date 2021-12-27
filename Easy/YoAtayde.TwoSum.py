"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

# Option 1: Brute Froce
def twoSum(nums: list, target: int) -> list:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]

# Option 2: Two-pass Hash Table
def twoSum1(nums: list, target: int) -> list:
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap and hashmap[complement] != i:
            return [i, hashmap[complement]] 


# Option 3: One-pass Hash Table
def twoSum2(nums: list, target: int) -> list:
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i

nums = [2,7,11,15]
target = 9

print(twoSum(nums, target))
print(twoSum1(nums, target))
print(twoSum1(nums, target))