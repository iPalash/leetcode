# Link: https://leetcode.com/problems/max-consecutive-ones-iii/

## Example

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

## Constraints

- len<10^5
- k<=len

## Idea

- Keep start and curr & store all zeroes you encounter
- When number of zero exceed k pop the first zero in the list and reset start to its idx+1
- Missed a couple of edges cases around all zeroes and k being zero, be more careful of such cases going forward.
- A more elegant solutiton for this: https://leetcode.com/problems/max-consecutive-ones-iii/discuss/247564/JavaC%2B%2BPython-Sliding-Window - The premise is instead of having accurate indices for the window we move i,j both when necessary keeping the windows constant.
