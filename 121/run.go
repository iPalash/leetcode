package main

import (
	"fmt"
	"leetcode/common"
	"strconv"
	"strings"
)

func readPrices(input []string) []int {
	line := input[0]
	//ignore [] at the end
	prices := make([]int, 0)
	line = line[1 : len(line)-1]
	numbers := strings.Split(line, ",")
	// fmt.Println(numbers)
	for _, el := range numbers {
		price, err := strconv.Atoi(el)
		if err != nil {
			break
		}
		fmt.Println(el, price)
		prices = append(prices, price)
	}
	fmt.Println(prices)
	return prices
}

func maxProfit(prices []int) int {
	currMin := -1
	maxProf := 0
	for _, price := range prices {
		if currMin == -1 || price < currMin {
			currMin = price
		}
		currProf := price - currMin
		if currProf > 0 {
			if currProf > maxProf {
				maxProf = currProf
			}
		}
	}
	fmt.Println(maxProf)
	return maxProf
}

func main() {
	prices := readPrices(common.ReadInput())
	maxProfit(prices)
}
