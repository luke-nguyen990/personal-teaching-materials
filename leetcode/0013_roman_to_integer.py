# https://leetcode.com/problems/roman-to-integer/


class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        for i, v in enumerate(s):
            if v == 'I':
                ans += 1
            if v == 'V':
                ans += 5
                if i > 0 and s[i - 1] == 'I':
                    ans -= 2
            if v == 'X':
                ans += 10
                if i > 0 and s[i - 1] == 'I':
                    ans -= 2
            if v == 'L':
                ans += 50
                if i > 0 and s[i - 1] == 'X':
                    ans -= 20
            if v == 'C':
                ans += 100
                if i > 0 and s[i - 1] == 'X':
                    ans -= 20
            if v == 'D':
                ans += 500
                if i > 0 and s[i - 1] == 'C':
                    ans -= 200
            if v == 'M':
                ans += 1000
                if i > 0 and s[i - 1] == 'C':
                    ans -= 200
        return ans
