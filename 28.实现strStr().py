# 实现 strStr() 函数。
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。
# 如果不存在，则返回  -1。
# 示例 1:
# 输入: haystack = "hello", needle = "ll"
# 输出: 2
# 示例 2:
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack is None or needle is None:
            return -1
        for i in range(len(haystack)-len(needle)+1):
            if needle == haystack[i:i+len(needle)]:
                return i    
                break
        else:
            return -1