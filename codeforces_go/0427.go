package main

import (
	"fmt"
	"math"
)

func main() {
	var caseNum int
	fmt.Scan(&caseNum)
	arr := make([]float64, caseNum)
	for i := 0; i < caseNum; i++ {
		fmt.Scan((&arr[i]))
	}
	var ans float64 = 0
	var freePolice float64 = 0

	for i := 0; i < len(arr); i++ {
		var value float64 = arr[i]
		if value < 0 {
			ans += math.Max(0, -value-freePolice)

		}
		freePolice = math.Max(0, freePolice+value)
	}
	fmt.Println(ans)
}
