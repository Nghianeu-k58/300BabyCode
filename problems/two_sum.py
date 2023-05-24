"""
Two sum problems.

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Can you come up with an algorithm that is less than O(n^2) time complexity?
"""


class Solution:

    @staticmethod
    def solution(input_array, target):
        """Get and return 2 number with target."""
        checked_dict = dict()
        for index, number in enumerate(input_array):
            partner = target - number

            if partner in checked_dict:
                return [checked_dict[partner], index], "OK"

            checked_dict[number] = index
        return None, "Cannot find 2 numbers with input target"
