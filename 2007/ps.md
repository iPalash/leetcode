Link: https://leetcode.com/problems/find-original-array-from-doubled-array/

Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]
Explanation: One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].

Constraints:
changed.len<=10^5

Idea:
The first idea was a linear scan from i+1 to n for num*2
That was too slow

The second was to reduce it to log time by using binary search after sorting the array
This reached 20% perf but can still be improved upon
!TODO do this faster.