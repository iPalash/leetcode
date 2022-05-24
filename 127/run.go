package main

import (
	"fmt"
	"leetcode/common"
	"strings"
)

func read() (string, string, []string) {
	var begin, end string
	var list []string
	inp := common.ReadInput()
	begin = common.StripQuotes(inp[0])
	end = common.StripQuotes(inp[1])
	for _, el := range strings.Split(common.StripSquareBracketsFromEnd(inp[2]), ",") {
		list = append(list, common.StripQuotes(el))
	}
	return begin, end, list
}

func Diff(s1, s2 byte) int {
	// fmt.Println(s1, int(s1), s2, int(s2))
	if s1 == s2 {
		return 0
	} else {
		return 1
	}
}

func adjacent(s1, s2 string) bool {
	diff := 0
	for idx, _ := range s1 {
		diff += Diff(s1[idx], s2[idx])
	}
	return diff == 1
}

type Graph struct {
	// Vertices []int
	N     int
	Edges map[int]map[int]bool
}

func ConstructGraph(begin string, list []string) *Graph {
	//Let's use n to represent begin word
	n := len(list)
	g := &Graph{N: n}
	edges := make(map[int]map[int]bool)
	g.Edges = edges
	g.Edges[n] = make(map[int]bool)
	for i, word := range list {
		g.Edges[i] = make(map[int]bool)
		if adjacent(begin, word) {
			g.Edges[i][n] = true
			g.Edges[n][i] = true
		}
		for j, word2 := range list {
			if i != j && adjacent(word, word2) {
				g.Edges[i][j] = true
			}
		}
	}
	// fmt.Println(g.Edges)
	return g
}

func CheckInList(end string, list []string) int {
	for idx, word := range list {
		if end == word {
			return idx
		}
	}
	return -1
}

func bfs(g *Graph, start, end int) int {
	type Node struct {
		Idx   int
		Depth int
	}
	var toBeVisited []Node
	visitedMap := make(map[int]bool)
	toBeVisited = append(toBeVisited, Node{Idx: start, Depth: 0})
	for len(toBeVisited) > 0 {
		// fmt.Println(toBeVisited)
		//Pop the first element
		curr := toBeVisited[0]
		toBeVisited = toBeVisited[1:]
		visitedMap[curr.Idx] = true
		for k := range g.Edges[curr.Idx] {
			if _, ok := visitedMap[k]; !ok {
				toBeVisited = append(toBeVisited, Node{k, curr.Depth + 1})
				visitedMap[k] = true
				if k == end {
					return curr.Depth + 1
				}
			}
		}
	}
	return -1
}

func ladderLength(beginWord string, endWord string, wordList []string) int {
	// fmt.Println(beginWord, endWord, wordList)
	endIdx := CheckInList(endWord, wordList)
	if endIdx == -1 {
		return 0
	}
	g := ConstructGraph(beginWord, wordList)
	return 1 + bfs(g, len(wordList), endIdx)
	// return 0
}

func main() {
	begin, end, list := read()
	fmt.Println(ladderLength(begin, end, list))
}
