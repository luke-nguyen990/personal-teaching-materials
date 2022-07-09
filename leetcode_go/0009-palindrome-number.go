//https://leetcode.com/problems/palindrome-number/
package leetcodego

func isPalindrome(x int) bool {
	reversedNum := 0
	temp := x
	for temp > 0 {
		reversedNum = reversedNum*10 + temp%10
		temp = temp / 10
	}
	return x == reversedNum
}
