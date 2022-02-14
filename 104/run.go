package main

import (
	"fmt"
	"leetcode/common"
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

func read() *TreeNode {
	nums := common.ReadArrayWithNils()
	if len(nums) == 0 {
		return nil
	}
	root := &TreeNode{Val: *nums[0]}
	var nodes []*TreeNode
	nodes = append(nodes, root)
	for i, num := range nums[1:] {
		if num != nil {
			curr := &TreeNode{Val: *num}
			nodes = append(nodes, curr)
			parentIdx := int((i + 2) / 2)
			// fmt.Println(parentIdx)
			if (i+2)%2 == 0 {
				//Even 1-based index, so left child of (i+1)//2
				nodes[parentIdx-1].Left = curr
			} else {
				nodes[parentIdx-1].Right = curr
			}
		}
	}
	// fmt.Println(nodes, nums)
	return root
}

func MaxInt(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func maxDepth(node *TreeNode) int {
	if node == nil {
		return 0
	}
	// fmt.Println(node.Val)
	return 1 + MaxInt(maxDepth(node.Left), maxDepth(node.Right))
}

func main() {
	fmt.Println(maxDepth(read()))
}
