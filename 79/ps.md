# Link: <https://leetcode.com/problems/word-search/>

## Example

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

## Constraints

- 1<= m,n,<=6
- word.len<=15

## Idea

- A simple dfs starting when letter matches the word
- My idea was of pruning was only going to matching text, can we do better?
