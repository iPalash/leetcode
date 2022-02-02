package main

import (
	"fmt"
	"leetcode/common"
	"strconv"
	"strings"
)

func readTriangle(input []string) [][]int {
	line := input[0]
	//ignore [] at the end
	prices := make([][]int, 0)
	line = line[2 : len(line)-2]
	rows := strings.Split(line, "],[")

	for _, el := range rows {
		// itemStr := el[1 : len(el)-1]
		items := strings.Split(el, ",")
		itemArr := make([]int, 0)
		// fmt.Println(items)
		for _, num := range items {
			price, err := strconv.Atoi(num)
			if err == nil {
				itemArr = append(itemArr, price)
			}
		}
		prices = append(prices, itemArr)
	}
	// fmt.Println(prices)
	return prices
}

func mn(a, b int) int {
	if a < b {
		return a
	} else {
		return b
	}
}

func minimumTotal_nsquare(triangle [][]int) int {
	dp := make([][]int, 0)
	n := len(triangle)
	first := []int{triangle[0][0]}
	dp = append(dp, first)
	// fmt.Println(triangle, dp, dp[0][0], triangle[1][0])
	for i := 1; i < n; i++ {
		arr := make([]int, i+1)
		dp = append(dp, arr)
		for j := 0; j <= i; j++ {
			// fmt.Println(i, j, dp)
			if j == 0 {
				dp[i][j] = dp[i-1][j] + triangle[i][j]
			} else {
				// two cases here too:
				// case 1: when jth element exists in i: j<i
				// case 2: when j=i
				if j < i {
					dp[i][j] = mn(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
				} else {
					dp[i][j] = dp[i-1][j-1] + triangle[i][j]
				}
			}

		}
		// fmt.Println(dp)
	}
	ans := dp[n-1][0]
	for _, el := range dp[n-1] {
		if el < ans {
			ans = el
		}
	}
	fmt.Println(ans)
	return ans

}

func minimumTotal(triangle [][]int) int {

	n := len(triangle)
	dp1 := make([]int, n)
	dp2 := make([]int, n)
	dp1[0] = triangle[0][0]
	dp2[0] = triangle[0][0]
	// fmt.Println(triangle, dp, dp[0][0], triangle[1][0])
	for i := 1; i < n; i++ {
		for j := 0; j <= i; j++ {
			// fmt.Println(i, j, dp1, dp2)
			if j == 0 {
				dp2[j] = dp1[j] + triangle[i][j]
			} else {
				// two cases here too:
				// case 1: when jth element exists in i: j<i
				// case 2: when j=i
				if j < i {
					dp2[j] = mn(dp1[j], dp1[j-1]) + triangle[i][j]
				} else {
					dp2[j] = dp1[j-1] + triangle[i][j]
				}
			}
			fmt.Println(i, j, dp1, dp2)

		}
		copy(dp1, dp2)
		// fmt.Println(i, dp1, dp2)
	}
	// fmt.Print(dp)
	ans := dp2[0]
	for _, el := range dp2 {
		if el < ans {
			ans = el
		}
	}
	fmt.Println(ans)
	return ans

}

func main() {
	triangle := readTriangle(common.ReadInput())
	minimumTotal(triangle)
}
