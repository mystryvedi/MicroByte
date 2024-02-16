# 1481 Least Number of Unique Integers after K Removals

# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

 

# Example 1:

# Input: arr = [5,5,4], k = 1
# Output: 1
# Explanation: Remove the single 4, only 5 is left.
# Example 2:
# Input: arr = [4,3,1,1,3,3,2], k = 3
# Output: 2
# Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
 

# Constraints:

# 1 <= arr.length <= 10^5
# 1 <= arr[i] <= 10^9
# 0 <= k <= arr.length

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = {}
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        l = sorted(d.items(), key = lambda x:x[1])
        for i in range(len(l)):
            if k<=0:
                break
            else:
                d[l[i][0]]-=k
                k-=l[i][1]
        count = 0
        for i in d:
            if d[i]>0:
                count+=1
        return count
