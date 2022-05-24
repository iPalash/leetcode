package main

import (
	"fmt"
	"leetcode/common"
	"strconv"
	"strings"
)

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func readBinaryTree(input []string) *TreeNode {
	//Input example: [2,3,1,3,1,null,1]

	//take just the first line
	line := input[0]
	//ignore [] at the end
	line = line[1 : len(line)-1]
	rows := strings.Split(line, ",")
	treeMap := make(map[int]*TreeNode)
	//For every node this holds whether ith digit count is odd or even
	// 0=> even, 1=>odd
	dp := make([][]int, len(rows))
	for i := 0; i < len(rows); i++ {
		dp[i] = make([]int, 10)
	}
	var root *TreeNode

	//left child would be at loc 2*(i+1)-1
	//right would at 2*(i+1) //zero-based indexing
	for i, el := range rows {
		fmt.Println(i, el)
		val, _ := strconv.Atoi(el)
		if root == nil {
			//setting root node
			curr := &TreeNode{Val: val}
			fmt.Println("root is", val)
			treeMap[i] = curr
			//Flip 0 to 1 or reverse , must be a bit way to doing this
			dp[i][val] = 1
			root = curr
		} else if el != "null" {
			//normal node
			curr := &TreeNode{Val: val}
			treeMap[i] = curr
			//Set the corresponding child in parent
			//Parent would be (i+1)/2 - 1
			//if i+1 is even -> left else odd -> right
			parentIdx := (i+1)/2 - 1
			if (i+1)%2 == 0 {
				//even
				treeMap[parentIdx].Left = curr
				copy(dp[i], dp[parentIdx])
				dp[i][val] = (dp[i][val] + 1) % 2
				// fmt.Println("left of _ is _ ", treeMap[parentIdx].Val, val)
			} else {
				//odd
				treeMap[parentIdx].Right = curr
				copy(dp[i], dp[parentIdx])
				dp[i][val] = (dp[i][val] + 1) % 2
				// fmt.Println("right of _ is _ ", treeMap[parentIdx].Val, val)
			}

		} else if el == "null" {
			//empty node
		}
	}
	return root
}

func dfs(node *TreeNode, dp []int, height int) int {
	newdp := make([]int, 10)
	left := 0
	curr := 0
	right := 0
	copy(newdp, dp)
	// fmt.Println(newdp, node.Val)
	newdp[node.Val] = (newdp[node.Val] + 1) % 2
	if node.Left != nil {
		left = dfs(node.Left, newdp, height+1)
	}
	if node.Right != nil {
		right = dfs(node.Right, newdp, height+1)
	}

	//Leaf node
	if node.Left == nil && node.Right == nil {
		if height%2 == 0 {
			// fmt.Println("leaf even", node.Val, height)
			//even =>all must be even ie zero
			check := true
			for _, el := range newdp {
				if el != 0 {
					check = false
				}
			}
			if check {
				fmt.Println("found even", node.Val)
				curr = 1
			}
		} else {
			//odd =>all must be even except one
			// fmt.Println("leaf odd", node.Val, height)
			check := true
			odd := false // one odd required
			for _, el := range newdp {
				if el != 0 {
					if !odd {
						//first time odd
						odd = true
					} else {
						//getting multiples odds
						check = false
					}
				}
			}
			if check {
				fmt.Println("found odd", node.Val)
				curr = 1
			}
		}
	}
	return left + right + curr
}

func pseudoPalindromicPaths(root *TreeNode) int {
	dp := make([]int, 10)
	return dfs(root, dp, 1)
}

func main() {
	root := readBinaryTree(common.ReadInput())
	fmt.Println(pseudoPalindromicPaths(root))
}
