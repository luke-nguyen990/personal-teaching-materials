//https://codeforces.com/contest/1352/problem/A
package main

import (
	. "fmt"
)

func main() {
	var t, n int
	for Scan(&t); t > 0; t-- {
		Scan(&n)
		a := []interface{}{}
		for i := 1; n > 0; n /= 10 {
			if n%10 > 0 {
				a = append(a, n%10*i)
			}
			i *= 10
		}
		Println(len(a))
		Println(a...)
	}
}
