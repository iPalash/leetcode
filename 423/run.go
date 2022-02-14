package main

import (
	"fmt"
	"leetcode/common"
	"sort"
	"strings"
)

/*
0 - zero
1 - one
2 - two
3 - three
4 - four
5 - five
6 - six
7 - seven
8 - eight
9 - nine

0 - z
2 - w
3 - h
4 - u
6 - x
8 - g
7 - s (-6)
5 - f (-4)
9 - i (-6,-8)
1 - o (rest)
*/

func removeAt(s string, i int) string {
	return s[:i] + s[i+1:]
}

func replaceAt(s string, i int, b string) string {
	return s[:i] + b + s[i+1:]
}

func find(digits map[byte][]int, letter byte, digit int) int {
	if k, ok := digits[letter]; ok && len(k) > 0 {
		first := digits[letter][0]
		return first
	} else {
		return -1
	}
}

func getSpell(digit int) string {
	switch digit {
	case 0:
		return "zero"
	case 1:
		return "one"
	case 2:
		return "two"
	case 3:
		return "three"
	case 4:
		return "four"
	case 5:
		return "five"
	case 6:
		return "six"
	case 7:
		return "seven"
	case 8:
		return "eight"
	case 9:
		return "nine"
	}
	return ""
}

/*
0 - z
2 - w
3 - h
4 - u
6 - x
8 - g
7 - s (-6)
5 - f (-4)
9 - i (-6,-8)
1 - o (rest)
*/

type Mapper struct {
	Digit int
	Char  byte
}

func mapper() []Mapper {
	return []Mapper{{0, 'z'}, {2, 'w'}, {4, 'u'}, {6, 'x'}, {8, 'g'}, {3, 'h'}, {7, 's'}, {5, 'f'}, {9, 'i'}, {1, 'o'}}
}

func removeCharForDigit(digits map[byte][]int, s string, digit int) (string, map[byte][]int) {
	word := getSpell(digit)
	var idx []int
	// fmt.Println(digit, word)
	for i, _ := range word {
		idx = append(idx, digits[word[i]][0])

		s = replaceAt(s, digits[word[i]][0], "$")
		digits[word[i]] = digits[word[i]][1:]
	}
	return s, digits
}

func originalDigits(s string) string {
	mp := make(map[byte][]int)
	for i := range s {
		// fmt.Println(char(s[i]))
		if _, ok := mp[s[i]]; ok {
			mp[s[i]] = append(mp[s[i]], i)
		} else {
			mp[s[i]] = []int{i}
		}
	}
	// fmt.Println(mp)
	digitMap := mapper()
	var ans []int
	for len(strings.ReplaceAll(s, "$", "")) > 0 {
		// fmt.Println(s)
		for i := 0; ; {
			//Look for chr for digit
			el := digitMap[i]
			// fmt.Println(el.Digit, el.Char, s)
			// fmt.Println(string(el.Char), el.Digit)
			z := find(mp, el.Char, el.Digit)
			if z != -1 {
				// fmt.Println(digit, chr, z)
				ans = append(ans, el.Digit)
				s, mp = removeCharForDigit(mp, s, el.Digit)
				if len(strings.ReplaceAll(s, "$", "")) == 0 {
					break
				}
			} else {
				i += 1
			}
		}

	}
	sort.Ints(ans)
	ansString := ""
	for _, el := range ans {
		ansString += fmt.Sprint(el)
	}
	return ansString
}

func main() {
	inp := common.ReadInput()[0]
	//Remove quote
	inp = common.StripQuotes(inp)
	fmt.Println(originalDigits(inp))
}
