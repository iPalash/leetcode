# Link: https://leetcode.com/problems/factor-combinations/

## Example

## Constraints

- n<10^7

## Idea

- Get the prime factorisation of the number
- Pick a prime, either multiply with the remaining (next chosen must be greater than equal) or break it at curr and addd the next factor as another multiplier in the series
- Discard all series which aren't increasing to avoid duplicates
