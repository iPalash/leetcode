Link: https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/


Input: s = "havefunonleetcode", k = 5
Output: 6
Explanation: There are 6 substrings they are: 'havef','avefu','vefun','efuno','etcod','tcode'.

Constraints:
all lowercase letters


Idea:
start with i and j 
reset i to first repeat+1 when found and update counts