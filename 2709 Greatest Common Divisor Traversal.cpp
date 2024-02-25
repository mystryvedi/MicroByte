// 2709 Greatest Common Divisor Traversal

// You are given a 0-indexed integer array nums, and you are allowed to traverse between its indices. You can traverse between index i and index j, i != j, if and only if gcd(nums[i], nums[j]) > 1, where gcd is the greatest common divisor.

// Your task is to determine if for every pair of indices i and j in nums, where i < j, there exists a sequence of traversals that can take us from i to j.

// Return true if it is possible to traverse between all such pairs of indices, or false otherwise.

 

// Example 1:

// Input: nums = [2,3,6]
// Output: true
// Explanation: In this example, there are 3 possible pairs of indices: (0, 1), (0, 2), and (1, 2).
// To go from index 0 to index 1, we can use the sequence of traversals 0 -> 2 -> 1, where we move from index 0 to index 2 because gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1, and then move from index 2 to index 1 because gcd(nums[2], nums[1]) = gcd(6, 3) = 3 > 1.
// To go from index 0 to index 2, we can just go directly because gcd(nums[0], nums[2]) = gcd(2, 6) = 2 > 1. Likewise, to go from index 1 to index 2, we can just go directly because gcd(nums[1], nums[2]) = gcd(3, 6) = 3 > 1.
// Example 2:

// Input: nums = [3,9,5]
// Output: false
// Explanation: No sequence of traversals can take us from index 0 to index 2 in this example. So, we return false.
// Example 3:

// Input: nums = [4,3,12,8]
// Output: true
// Explanation: There are 6 possible pairs of indices to traverse between: (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), and (2, 3). A valid sequence of traversals exists for each pair, so we return true.
 

// Constraints:

// 1 <= nums.length <= 105
// 1 <= nums[i] <= 105

class unionFind{
    public:
    vector<int> parent;
    vector<int> rank;
    
    unionFind(int n)
    {
        parent = vector<int> (n);
        for(int i=0;i<n;i++) parent[i] = i;
        rank = vector<int> (n,0);
    }
    
    int findParent(int i)
    {
        if(i==parent[i]) return i;
        
        return parent[i] = findParent(parent[i]);
    }
    
    bool areconnected(int i,int j)
    {
        return (findParent(i)==findParent(j));
    }
    bool unify(int i,int j)
    {
        i = findParent(i);
        j = findParent(j);
        
        if(i==j) return false;
        
        if(rank[i]>rank[j])
        {
            parent[j] = i;
            rank[i]++;
        }
        else
        {
            parent[i] = j;
            rank[j]++;
        }
        
        return true;
    }
    
    int components()
    {
        int count = 0;
        for(int i = 0;i<parent.size();i++)
        {
            if(i==parent[i]) count++;
        }
        return count;
    }

};

class Solution {
public:
    bool canTraverseAllPairs(vector<int>& nums) {
        int n = nums.size();
        unionFind uf(n);
        
        unordered_map<int,vector<int>> adj;

        for(int i=0;i<n;i++)
        {
            int num = nums[i];

            if((num&1)==0) adj[2].push_back(i);
            while((num&1)==0) num/=2;

            for(int j=3;j*j<=num;j+=2)
            {
                if(num%j==0) adj[j].push_back(i);
                while(num%j==0) num/=j;
            }

            if(num>2) adj[num].push_back(i);
            
        }

        for(auto [key,vec] : adj)
        {
            for(int i=1;i<vec.size();i++)
            {
                uf.unify(vec[0],vec[i]);
            }
        }
        
        return uf.components()==1? true : false;
    }
};
