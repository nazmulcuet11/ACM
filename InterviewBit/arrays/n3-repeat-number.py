class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        cnt = [0, 0, 0]
        val = [0, 0, 0]
        for number in A:
            found = False
            for i in range(3):
                if cnt[i] != 0 and val[i] == number:
                    cnt[i] += 1
                    found = True
                    break
            
            if not found:
                for i in range(3):
                    if cnt[i] == 0:
                        val[i] = number
                        cnt[i] = 1 
                        break
 
            if cnt[i] > 0 and cnt[1] > 0 and cnt[2] > 0:
                for i in range(3):
                    cnt[i] -= 1

        for i in range(3):
            if cnt[i] > 0:
                cntNumber = 0
                for number in A:
                    if number == val[i]:
                        cntNumber += 1
                if cntNumber > len(A) / 3:
                    return val[i]

        return -1

# print(Solution().repeatedNumber([1, 2, 3, 1, 1]))
print(Solution().repeatedNumber([ 1000441, 1000441, 1000994 ]))
# print(Solution().repeatedNumber([1, 1, 1, 2, 3, 5, 7 ]))
# print(Solution().repeatedNumber([ 1000727, 1000727, 1000641, 1000517, 1000212, 1000532, 1000727, 1001000, 1000254, 1000106, 1000405, 1000100, 1000736, 1000727, 1000727, 1000787, 1000105, 1000713, 1000727, 1000333, 1000069, 1000727, 1000877, 1000222, 1000727, 1000505, 1000641, 1000533, 1000727, 1000727, 1000727, 1000508, 1000475, 1000727, 1000573, 1000727, 1000618, 1000727, 1000309, 1000486, 1000792, 1000727, 1000727, 1000426, 1000547, 1000727, 1000972, 1000575, 1000303, 1000727, 1000533, 1000669, 1000489, 1000727, 1000329, 1000727, 1000050, 1000209, 1000109 ]))