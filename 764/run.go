package main

import (
	"fmt"
	"leetcode/common"
	"strconv"
	"strings"
)

func readGrid(input []string) (int, [][]int) {
	fmt.Println(input)

	line1 := input[0]
	n, _ := strconv.Atoi(line1)

	line := input[1]
	mines := make([][]int, 0)
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
		mines = append(mines, itemArr)
	}
	return n, mines
}

func main() {
	n, mines := readGrid(common.ReadInput())
	fmt.Println(n, mines)

	orderOfLargestPlusSign(n, mines)
}

func orderOfLargestPlusSign(n int, mines [][]int) int {

	grid := make([][]int, n)
	for i := 0; i < n; i++ {
		grid[i] = make([]int, n)
	}
	// fmt.Println(grid)
	for _, mine := range mines {
		grid[mine[0]][mine[1]] = -1
	}
	// fmt.Println(mineMap)
	L := make([][]int, n)
	R := make([][]int, n)
	U := make([][]int, n)
	D := make([][]int, n)

	//start top left at 0,0 and going row wise

	for i := 0; i < n; i++ {
		R[i] = make([]int, n)
		U[i] = make([]int, n)
		for j := 0; j < n; j++ {
			// fmt.Println(i, j)
			if grid[i][j] == -1 {
				R[i][j] = 0
				U[i][j] = 0
				continue
			}
			if j == 0 {
				R[i][j] = 1
			} else {
				R[i][j] = 1 + R[i][j-1]
			}
			if i == 0 {
				U[i][j] = 1
			} else {
				U[i][j] = 1 + U[i-1][j]
			}

		}
	}

	//start bottom right at n-1,n-1 and going row wise reverse

	for i := n - 1; i >= 0; i-- {
		L[i] = make([]int, n)
		D[i] = make([]int, n)
		for j := n - 1; j >= 0; j-- {
			// fmt.Println(i, j, D[i])
			if grid[i][j] == -1 {
				L[i][j] = 0
				D[i][j] = 0
				continue
			}
			if j == n-1 {
				L[i][j] = 1
			} else {
				L[i][j] = 1 + L[i][j+1]
			}
			if i == n-1 {
				D[i][j] = 1
			} else {
				D[i][j] = 1 + D[i+1][j]
			}

		}
	}
	// fmt.Printf("%v\n%v\n%v\n%v\n", L, R, U, D)
	maxPlusSize := 0
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			mn := L[i][j]
			if U[i][j] < mn {
				mn = U[i][j]
			}
			if R[i][j] < mn {
				mn = R[i][j]
			}
			if D[i][j] < mn {
				mn = D[i][j]
			}
			if mn != 0 && mn > maxPlusSize {
				// fmt.Println(i, j, mn)
				maxPlusSize = mn
			}
		}
	}
	fmt.Println(maxPlusSize)
	return maxPlusSize
}
