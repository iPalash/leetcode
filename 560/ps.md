Link: https://leetcode.com/problems/subarray-sum-equals-k/

Input: nums = [1,2,3], k = 3
Output: 2

Idea:
Just compute prefixSum array and find j for every i such that
pr[i]+k=pr[j] && j>i, then array in [i,j)
This can be done using a hashmap

