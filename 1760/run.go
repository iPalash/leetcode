package main

import (
	"fmt"
	"leetcode/common"
	"sort"
)

func MaxInt(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func minimumSize(nums []int, maxOperations int) int {
	for maxOperations > 0 {
		sort.Ints(nums)
		fmt.Println(nums, maxOperations)
		n := len(nums)
		last := nums[n-1]
		if last == 1 {
			break
		}

		//get a x which breaks last but is greater than second_last
		

		x := int(last / (maxOperations + 1))
		// if n > 1 {
		// 	//Get Number just smaller than last
		// 	idx := n - 2
		// 	for nums[idx] == last && idx >= 0 {
		// 		idx--
		// 	}
		// 	if nums[idx] != last {
		// 		second_largest := nums[idx]
		// 		x = MaxInt(x, second_largest)
		// 	}
		// }
		y := last - x
		// fmt.Println(maxOperations, last, x, y)
		nums = nums[:n-1]
		nums = append(nums, x, y)
		maxOperations -= 1
	}
	sort.Ints(nums)
	return nums[len(nums)-1]
}

func binary(nums []int, i, j, el int) int {
	mid := (i + j) / 2
	// fmt.Println(nums[i:], el, i, mid, j)

	if i > j {
		return -1
	} else if nums[mid] == el {
		return mid
	} else if nums[mid] < el {
		return binary(nums, mid+1, j, el)
	} else {
		return binary(nums, i, mid-1, el)
	}
}

func main() {
	nums, k := common.ReadArrayAndN()
	fmt.Println(minimumSize(nums, k))
}
