package common

import (
	"bufio"
	"encoding/json"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func ReadInput() []string {
	input := make([]string, 0)
	scanner := bufio.NewScanner(os.Stdin)
	for {
		//scan a line
		scanner.Scan()
		text := scanner.Text()
		if len(text) != 0 {
			input = append(input, text)
		} else {
			break
		}
	}
	return input
}

func ReadArrayAndN() ([]int, int) {
	s := ReadInput()
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

func MaxInt(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func MinInt(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func PrettyPrint(v interface{}) {
	b, err := json.Marshal(v)
	if err == nil {
		fmt.Println(string(b))
	}
}
