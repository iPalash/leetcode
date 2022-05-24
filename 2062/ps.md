Link:https://leetcode.com/problems/count-vowel-substrings-of-a-string/


Input: word = "aeiouu"
Output: 2
Explanation: The vowel substrings of word are as follows (underlined):
- "aeiouu"
- "aeiouu"

Input: word = "cuaieuouac"
Output: 7
Explanation: The vowel substrings of word are as follows (underlined):
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"

Constraints:
- 1<=word.length<=100
- only english lowercase letters


Idea:
Keep iterating until one hits all vowels
That's the first world
If the next letter is also vowel
aeiouaeiou =>


Find the smallest sequence starting at i which contains all 5 vowels : Num of words = (last contiguos vowel - last word index) + 1
i=> world strt index
j=> world end index
k=>last contiguous vowel

