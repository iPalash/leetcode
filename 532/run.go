package main

// import (
// 	"fmt"
// 	"leetcode/common"
// 	"sort"
// 	"strconv"
// 	"strings"
// )

// func read(s []string) ([]int, int) {
// 	//Removing the []
// 	arr := strings.Split(s[0][1:len(s[0])-1], ",")
// 	var nums []int
// 	for _, v := range arr {
// 		tmp, _ := strconv.Atoi((v))
// 		nums = append(nums, tmp)
// 	}
// 	tmp, _ := strconv.Atoi(s[1])
// 	return nums, tmp
// }

// func binary(nums []int, i, j, el int) int {
// 	mid := (i + j) / 2
// 	// fmt.Println(nums[i:], el, i, mid, j)

// 	if i > j {
// 		return -1
// 	} else if nums[mid] == el {
// 		return mid
// 	} else if nums[mid] < el {
// 		return binary(nums, mid+1, j, el)
// 	} else {
// 		return binary(nums, i, mid-1, el)
// 	}
// }

// func findPairs(nums []int, k int) int {
// 	fmt.Println(nums, k)
// 	sort.Ints(nums)
// 	n := len(nums)
// 	unique := make(map[int]bool)
// 	ans := 0
// 	for idx, num := range nums {
// 		if binary(nums, idx+1, n-1, num+k) != -1 {
// 			if _, ok := unique[num]; !ok {
// 				// fmt.Println(num, num+k)
// 				unique[num] = true
// 				ans += 1
// 			}
// 		}
// 	}

// 	return ans
// }

// func main() {
// 	nums, k := read(common.ReadInput())
// 	fmt.Println(findPairs(nums, k))
// }
