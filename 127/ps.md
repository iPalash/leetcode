Link: https://leetcode.com/problems/word-ladder/

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.


Constraints:
word length b/w 1-10
endW.len == beginW.len
wordList.len <= 5000
wordList[i].len==beginWord.len

Idea:

Simple bfs to see if endWord is reachable
Depth (+1) would be the answer 

Quite slow, can we do better? !TODO 

Best according to lc, seems to be bidrectional bfs