# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:
# Input: ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: ["dog","racecar","car"]
# Output: ""

# Explanation: There is no common prefix among the input strings.


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        for i, var in enumerate(zip(*strs)):
            if len(set(var)) > 1:
                return strs[0][:i]
        else:
            return min(strs)


if __name__ == '__main__':
    common = Solution()
    print(common.longestCommonPrefix(["flower","flow","flight"]))
