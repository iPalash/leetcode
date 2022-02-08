Link: https://leetcode.com/problems/word-pattern/

Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Input: pattern = "abba", s = "dog cat cat fish"
Output: false

The trick here was checking for bijection we need to verify both sides just a single map won't do

An extension of this question might be considering multi-letter patterns to fit the word list
