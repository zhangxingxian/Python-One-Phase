# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:
# Input: 123
# Output: 321

# Example 2:
# Input: -123
# Output: -321

# Example 3:
# Input: 120
# Output: 21

# Note:
#       Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For
#       the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        newNUM = 0
        flag = x < 0   # 检查x正负保存状态

        xAbs = abs(x)
        while xAbs != 0:
            newNUM = newNUM * 10 + xAbs % 10
            xAbs = xAbs //10
        if x > 2**31 -1:
            return 0
        return newNUM if not flag else -newNUM

if __name__ == '__main__':
    newNUM = Solution()
    print(newNUM.reverse(-1234567890))
    
    
    