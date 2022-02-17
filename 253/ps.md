# Link: <https://leetcode.com/problems/meeting-rooms-ii/>

## Example

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

## Constraints

- start,end^6

## Idea

Simple sorting works here
Sort the intervals first once to ensure the second sorting keeps end time before start time
Since overlap on start and end isn't considered an extra room