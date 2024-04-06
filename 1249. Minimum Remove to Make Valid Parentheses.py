# 1249. Minimum Remove to Make Valid Parentheses

# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
 
# Example 1:

# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# Example 2:

# Input: s = "a)b(c)d"
# Output: "ab(c)d"
# Example 3:

# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
 
# Constraints:

# 1 <= s.length <= 105
# s[i] is either'(' , ')', or lowercase English letter.

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_count = 0
        close_count = 0
        flag = 0
        ans = ""
        
        for char in s:
            if char == '(':
                open_count += 1
                flag += 1
            elif char == ')' and flag > 0:
                close_count += 1
                flag -= 1
        
        k = min(open_count, close_count)
        open_count = k
        close_count = k
        
        for char in s:
            if char == '(':
                if open_count > 0:
                    ans += '('
                    open_count -= 1
                continue
            if char == ')':
                if close_count > 0 and close_count > open_count:
                    ans += ')'
                    close_count -= 1
                continue
            else:
                ans += char
        
        return ans
