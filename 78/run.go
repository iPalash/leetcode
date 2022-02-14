package main

import (
	"fmt"
	"leetcode/common"
)

func subsets(nums []int) [][]int {
	var ans [][]int
	n := len(nums)
	for i := 0; i < 1<<n; i++ {
		var tmp []int
		for j := 0; j < n; j++ {
			if (i>>j)&1 == 1 {
				tmp = append(tmp, nums[j])
			}
		}
		ans = append(ans, tmp)
	}
	return ans
}

func main() {
	inp := common.ReadArray()
	ans := subsets(inp)
	// fmt.Println(len(ans))
	fmt.Println(ans)
}
