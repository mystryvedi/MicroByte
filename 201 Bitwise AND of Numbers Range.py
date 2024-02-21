# Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

 

# Example 1:

# Input: left = 5, right = 7
# Output: 4
# Example 2:

# Input: left = 0, right = 0
# Output: 0
# Example 3:

# Input: left = 1, right = 2147483647
# Output: 0
 

# Constraints:

# 0 <= left <= right <= 231 - 1

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if right-left==1: return left&right
        if left==right:return left
        a=bin(left)[2:]
        b=bin(right)[2:]
        if len(a)==len(b):
            s=''
            for i in range(len(a)):
                if a[i]==b[i]:
                    s+=a[i]
                else:break
            s+='0'*(len(a)-i)
            return int(s,2)
        return 0
