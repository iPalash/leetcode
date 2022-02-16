# Link: <https://leetcode.com/problems/maximum-number-of-points-with-cost/>

Input: points = [[1,2,3],[1,5,1],[3,1,1]]
Output: 9
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 2), (1, 1), and (2, 0).
You add 3 + 5 + 3 = 11 to your score.
However, you must subtract abs(2 - 1) + abs(1 - 0) = 2 from your score.
Your final score is 11 - 2 = 9.


## Constraints:

m,n<=10^5
m*n<10^5

## Idea:

Store best in dp[i][j]
such that dp[i][j] best score at row i at column j
take max on the last row for ans

this is o(m*n*n)

This was too slow for bigger cases

maintain just a best[cols] for adding to next row
This is same as m*n*n in impl

Took a hint
Maintain two arrays left and right for getting max at i from prev row

How to maintain this in linear time?
curr contains the best value at i so far

curr[i]=matrix[i]+max(left,right)

left[0]=curr[0]
left[i]=max(left[i-1]-1,curr[i])

right[n-1]=curr[n-1]
right[i]=max(curr[i],right[i+1]-1)

Breaking down the dp into left and right for getting sum makes this possible in linear time
