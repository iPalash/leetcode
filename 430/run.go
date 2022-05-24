package main

import (
	"fmt"
	"leetcode/common"
	"strconv"
	"strings"
)

/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Prev *Node
 *     Next *Node
 *     Child *Node
 * }
 */

type Node struct {
	Val   int
	Prev  *Node
	Next  *Node
	Child *Node
}

func GetArrayWithNils() []*int {
	inp := common.ReadInput()[0]
	arrStr := strings.Split(inp[1:len(inp)-1], ",")
	var arr []*int
	for _, el := range arrStr {
		if val, err := strconv.Atoi(el); err == nil {
			arr = append(arr, &val)
		} else {
			arr = append(arr, nil)
		}

	}
	return arr
}
func PrintLL(l []*Node) {
	for _, el := range l {
		fmt.Printf("%d, ", el.Val)
	}
	fmt.Println()
}
func readMultiLayerLL(arr []*int) *Node {
	var root *Node
	//First null would be the end of the current layer
	level := 0
	count := 0
	var prv, curr *Node
	var list []*Node
	for _, el := range arr {
		// if el == nil {
		// 	fmt.Println(nil, count, level)
		// } else {
		// 	fmt.Println(*el, count, level)
		// }
		// PrintLL(list)
		if root == nil {
			root = &Node{Val: *el}
			count += 1
			curr = root
			list = append(list, curr)
			prv = curr

		} else if level == 0 && el == nil {
			level += 1
			count = 0
			prv = nil
		} else if el != nil {
			//Same layer next node
			curr = &Node{Val: *el}
			if prv == nil && level > 0 {
				//First node which is not nil
				list[count].Child = curr
				list = []*Node{}
			} else {
				curr.Prev = prv
				prv.Next = curr
			}
			prv = curr
			list = append(list, curr)
			count += 1
		} else if level > 0 && el == nil {
			//Two cases :
			// 1. This is the null before the first node in the layer
			// 2. This is the end
			if prv == nil {
				//Case 1
				count += 1
			} else {
				//Case 2
				level += 1
				count = 0
				prv = nil
			}
		}
	}

	return root
}

func dfs(n *Node, prv *Node) *Node {
	if n == nil {
		return nil
	}
	curr := &Node{Val: n.Val}
	// fmt.Println(n.Val)
	curr.Prev = prv
	if prv != nil {
		prv.Next = curr
	}
	if n.Child != nil {
		curr = dfs(n.Child, curr)
	}
	if n.Next != nil {
		curr = dfs(n.Next, curr)
	}
	return curr
}

func flatten(root *Node) *Node {
	// var nr Node
	newTail := dfs(root, nil)
	curr := newTail
	// fmt.Println("here")
	for curr!=nil && curr.Prev != nil {
		// fmt.Println(curr.Val)
		curr = curr.Prev
	}
	return curr
}

func main() {
	arr := GetArrayWithNils()
	root := readMultiLayerLL(arr)
	fmt.Println(flatten(root))
}
