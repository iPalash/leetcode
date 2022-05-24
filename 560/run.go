package main

import (
	"fmt"
	"leetcode/common"
)

func subarraySum(nums []int, k int) int {
	mp := make(map[int]int)
	ans := 0
	sum := 0
	mp[0] = 1
	for _, num := range nums {
		sum += num
		// fmt.Println(num, mp)
		if v, ok := mp[sum-k]; ok {
			ans += v
		}
		if _, ok := mp[sum]; ok {
			mp[sum] += 1
		} else {
			mp[sum] = 1
		}

		//Let just calculate here only, so we can avoid checks for j>i which is extra
	}
	// for i := 0; i <= n; i++ {
	// 	val := k + prefix[i]
	// 	if v, ok := mp[val]; ok {
	// 		for idx, el := range v {
	// 			if el > i {
	// 				ans += len(v) - idx
	// 				break
	// 			}
	// 		}
	// 	}
	// }
	return ans
}

func main() {
	arr, n := common.ReadArrayAndN()
	fmt.Println(subarraySum(arr, n))
}
