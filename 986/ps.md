# Link: <https://leetcode.com/problems/interval-list-intersections/>

## Example

Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

## Constraints

- len<=1000
- start,end<10^9
- start<end

## Idea

- Sort the times and maintain two flag for open interval and add start when they are both true and end when one of them switches 
- This seemed straightforward to crack
- The soluton (m+n)log(m+n) while the given one is linear. !TODO Try the linear appraoch sometime later