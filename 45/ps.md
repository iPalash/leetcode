# Link: <https://leetcode.com/problems/jump-game-ii/>

## Example

- Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

## Constraints

- nums.len<10^4 

## Idea

- An n2 approach would be j[i]= min over j b/w (i+1,i+a[i]) of (j[j]) in reverse with j(n-1)=0
- The above was accepted but was slow
- The greedy approach was to jump to the position which maximizes the opportunity for the next jump.


