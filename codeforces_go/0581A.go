package main

import (
	"fmt"
	"math"
)

func main() {
	var a float64
	var b float64
	fmt.Scan(&a)
	fmt.Scan(&b)

	var ans1 int = int(math.Min(a, b))
	var ans2 int = int(math.Max(a, b)-math.Min(a, b)) / 2

	fmt.Printf("%d %d\n", ans1, ans2)
}
