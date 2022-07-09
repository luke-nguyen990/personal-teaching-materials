//https://leetcode.com/problems/two-sum/
package leetcodego

func twoSum(nums []int, target int) []int {
	dict := make(map[int]int)
	for index, num := range nums {
		i, found := dict[num]
		if found {
			return []int{i, index}
		}
		dict[target-num] = index
	}
	return []int{}
}
