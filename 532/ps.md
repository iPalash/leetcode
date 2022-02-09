Link: https://leetcode.com/problems/k-diff-pairs-in-an-array/

Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).


Idea:
Sort the array
Pick ith element and search for i+k to the right
(searching for i-k to the left isn't required since that would have already been discovered)

Simpler idea is to use a hashmap