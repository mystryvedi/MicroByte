# 85. Maximal Rectangle

# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

# Example 1:

# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 6
# Explanation: The maximal rectangle is shown in the above picture.
# Example 2:

# Input: matrix = [["0"]]
# Output: 0
# Example 3:

# Input: matrix = [["1"]]
# Output: 1
 
# Constraints:

# rows == matrix.length
# cols == matrix[i].length
# 1 <= row, cols <= 200
# matrix[i][j] is '0' or '1'.

def find_maximal_rectangle(matrix: list[list[str]]) -> int:
    m = len(matrix)
    n = len(matrix[0])
    heights = [0] * (n + 1)
    best = 0
    for row in matrix:
        for col in range(n):
            heights[col] = heights[col] + 1 if row[col] == '1' else 0
        stack = [-1]
        for col in range(n + 1):
            while heights[col] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = col - stack[-1] - 1
                best = max(best, h * w)
            stack.append(col)
    return best
if __name__ == '__main__':
    import json, sys
    with open('user.out', 'w') as f:
        for matrix in map(json.loads, sys.stdin):
            result = find_maximal_rectangle(matrix)
            print(result, file=f)
    sys.exit()
