package main

import (
	"fmt"
	"leetcode/common"
	"strings"
)

func wordPattern(pattern string, s string) bool {
	words := strings.Split(s, " ")
	patternMap := make(map[int]string)
	wordMap := make(map[string]byte)
	if len(words) != len(pattern) {
		return false
	}
	for idx, word := range words {
		fmt.Println(pattern[idx], word, patternMap, wordMap)
		if v, k := patternMap[int(pattern[idx])]; k {
			if v != word {
				return false
			}
		} else {
			patternMap[int(pattern[idx])] = word
		}
		if v, k := wordMap[word]; k {
			if v != pattern[idx] {
				return false
			}
		} else {
			wordMap[word] = pattern[idx]
		}
	}
	return true
}

func main() {
	inp := common.ReadInput()
	fmt.Println(wordPattern(inp[0][1:len(inp[0])-1], inp[1][1:len(inp[1])-1]))
}
