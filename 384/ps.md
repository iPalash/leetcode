# Link: <https://leetcode.com/problems/shuffle-an-array/>

## Example

Input
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
Output
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

Explanation
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // Shuffle the array [1,2,3] and return its result.
                       // Any permutation of [1,2,3] must be equally likely to be returned.
                       // Example: return [3, 1, 2]
solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]

## Constraints

- len<=200
- At most 5x10^4 calls to reset or shuffle

## Idea

- Seems straightforward, just randomly pick b/w i-n for the ith element and swap that with the ith
- Turns out this is a named algo Fisher Yates Algorithm
