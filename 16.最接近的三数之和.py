# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
# 找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = None
        for i in range(len(nums)-2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]
                if res is None or abs(sum3-target) < abs(res-target):
                    res = sum3
                if sum3 <= target:
                    l += 1
                else:
                    r -= 1
        return res