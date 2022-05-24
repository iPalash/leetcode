# Link: <https://leetcode.com/problems/find-all-anagrams-in-a-string/>

## Example

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

## Constraints

- s,p only lowercase letters

## Idea

- The idea was maintaing two pointers and moving them depending on current alphabets counts.
- only 40% perf, can we do better?
- The other way was similar but just move a fixed window and keep counting freq