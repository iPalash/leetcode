# Link: https://leetcode.com/problems/meeting-scheduler/

## Example

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
Output: [60,68]

## Constraints

- slots.len<10^4

## Idea

- Sort the slots
- Insert start of the longer len slots into an array
- For every start time in the second slots search for the matching one in first
- min(ends) - max(starts) > duration 
- Impl for this has too many edge cases, how to simplify this?
- Try a 2 pointer approach for this which linear complexity after sorting
- There is also a heap version of the solution which solves the subproblem of comparing while moving that caused so many edge case and twice pass necessary while doing binary search

!TODO !RETRY
