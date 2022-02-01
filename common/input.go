package common

import (
	"bufio"
	"os"
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
