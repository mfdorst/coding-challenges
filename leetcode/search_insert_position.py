#!/usr/bin/env python3

# https://leetcode.com/problems/search-insert-position/
#
# Given a sorted array of distinct integers and a target value, return the index if the target is
# found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
#
# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2
#
# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1
#
# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4
#
# Constraints:
# 1 <= nums.length <= 104
# -10^4 <= nums[i] <= 10^4
# nums contains distinct values sorted in ascending order.
# -10^4 <= target <= 10^4

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if len(nums) <= 3:
            return searchInsertShort(nums, target)
        mid = len(nums) // 2
        if target < nums[mid]:
            return self.searchInsert(nums[:mid], target)
        return mid + self.searchInsert(nums[mid:], target)

def searchInsertShort(nums: list[int], target: int) -> int:
    for i, num in enumerate(nums):
        if num >= target:
            return i
    return len(nums)
