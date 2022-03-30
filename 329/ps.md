# Link: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

## Example

## Constraints

- m,n<=200

## Idea

- Brute force, try all paths and backtrack when you cant
- Just a simple dfs with memorisation works here
- Trying topo sort as a preprocess, a technique called peeling onion, then we can use dp to solve this 
