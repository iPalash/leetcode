package main

import (
	"fmt"
	"leetcode/common"
)

func isVowel(s byte) int {
	switch s {
	case 'a':
		return 0
	case 'e':
		return 1
	case 'i':
		return 2
	case 'o':
		return 3
	case 'u':
		return 4
	default:
		return -1
	}
}

func allVowels(vowels []int) bool {
	return vowels[0] > 0 && vowels[1] > 0 && vowels[2] > 0 && vowels[3] > 0 && vowels[4] > 0
}

func countVowelSubstrings(word string) int {
	i := 0 //start
	j := 0 //end
	k := 0 //vowel curr
	currVowel := false
	vowels := make([]int, 5)
	n := len(word)
	fmt.Println(n)
	total := 0
	for i < n {
		fmt.Println(i, j, k)
		if isVowel(word[i]) != -1 {
			//Current is a vowel

			vowels[isVowel(word[i])] += 1

			// Starting counting j until we get allVowels or a consonant
			// When allVowels starting counting k from j
			// until a consonant or end is hit

			//Increment j until allVowels or end or consonant

			j = i + 1
			for j < n && !currVowel && isVowel(word[j]) != -1 {
				vowels[isVowel(word[j])] += 1
				currVowel = allVowels(vowels)
				j += 1
			}

			fmt.Println("j", i, j, k, vowels)

			if currVowel && k < n {
				k = j + 1
				for k < n && isVowel(word[k]) != -1 {
					k += 1
				}
				fmt.Println("counting", i, j, k, vowels)
				total += k - j
			}
			fmt.Println("k", i, j, k, vowels)

			if !currVowel {

				vowels[isVowel(word[i])] -= 1
				i += 1
			}

			for i <= j && currVowel {
				fmt.Println("i", i, j, k, vowels)
				vowels[isVowel(word[i])] -= 1
				i += 1
				currVowel = allVowels(vowels)
				if currVowel {
					fmt.Println("counting", i, j, k, vowels)
					total += k - j
				}
			}
			//After calculating the first word, need to move i keeping k and j fixed

			//If a consonant is found before we get allVowels, set i to j

		} else {
			vowels = []int{0, 0, 0, 0, 0}
			currVowel = false
			i += 1
		}
	}
	return total
}

func main() {
	fmt.Println(countVowelSubstrings(common.ReadInput()[0]))
}
