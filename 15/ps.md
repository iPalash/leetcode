# Link: <https://leetcode.com/problems/3sum/>

## Example

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

## Constraints

- nums.len<3000
- -10^5<=nums[i]<=10^5

## Idea

Sort the array
for every i,j look for k such that num[i]+num[j]=-num[k] and i,j,k are different
This can be done using two pointers and incrementing by incr i or decr by decreasing j

Checking for duplicates, first idea was around using a hash of tuples 
another easier way would be to play around with i and j when we find a match