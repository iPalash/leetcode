package main

import (
	"fmt"
	"leetcode/common"
	"sort"
	"strconv"
	"strings"
)

func read(s []string) ([]int, int) {
	//Removing the []
	arr := strings.Split(s[0][1:len(s[0])-1], ",")
	var nums []int
	for _, v := range arr {
		tmp, _ := strconv.Atoi((v))
		nums = append(nums, tmp)
	}
	tmp, _ := strconv.Atoi(s[1])
	return nums, tmp
}

func findPairs(nums []int, k int) int {
	fmt.Println(nums, k)
	sort.Ints(nums)
	// n := len(nums)
	unique := make(map[int]int)
	ans := 0
	for _, num := range nums {
		if _, ok := unique[num]; !ok {
			unique[num] = 1
		} else {
			unique[num] += 1
		}
	}

	for num, _ := range unique {
		if _, ok := unique[num+k]; ok {
			fmt.Println(num, num+k)
			if num == num+k && unique[num] > 1 {
				ans += 1
			} else if num != num+k {
				ans += 1
			}

		}
	}

	return ans
}

func main() {
	nums, k := read(common.ReadInput())
	fmt.Println(findPairs(nums, k))
}
