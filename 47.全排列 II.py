# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
# 示例:
# 输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]
import itertools
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = list(itertools.permutations(nums))
        return list(set(res))