Link: https://leetcode.com/problems/subsets/


Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]


Constraints:
1<=nums.len<=10
-10<=nums[i]<=10
All are unique

Idea:
2^n possible sets with each element having the choice of being included or not


Reimplemented usign the bit trick to generate all binary number of n digits

Use 1<<n instead math.pow for faster
1=>left shift => 10 : doubled
10 => right shift => 01 : halved