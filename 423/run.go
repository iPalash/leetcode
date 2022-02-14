package main

import (
	"fmt"
	"leetcode/common"
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

func getCount(mp map[byte]int, ch byte) int {
	if v, ok := mp[ch]; ok {
		return v
	} else {
		return 0
	}
}

func originalDigits(s string) string {
	count := make(map[byte]int)
	for i, _ := range s {
		if _, ok := count[s[i]]; ok {
			count[s[i]] += 1
		} else {
			count[s[i]] = 1
		}
	}
	counts := make([]int, 10)
	zero := count['z']
	two := count['w']
	four := count['u']
	six := count['x']
	eight := count['g']
	seven := count['s'] - six
	five := count['f'] - four
	three := count['h'] - eight
	nine := count['i'] - five - six - eight
	one := count['o'] - zero - two - four
	counts[0] = zero
	counts[1] = one
	counts[2] = two
	counts[3] = three
	counts[4] = four
	counts[5] = five
	counts[6] = six
	counts[7] = seven
	counts[8] = eight
	counts[9] = nine
	ans := ""
	for i, el := range counts {
		for j := 0; j < el; j++ {
			ans += fmt.Sprint(i)
		}
	}

	// fmt.Println(zero, one, two, three, four, five, six, seven, eight, nine)
	return ans
}

func main() {
	inp := common.ReadInput()[0]
	//Remove quote
	inp = common.StripQuotes(inp)
	fmt.Println(originalDigits(inp))
}
