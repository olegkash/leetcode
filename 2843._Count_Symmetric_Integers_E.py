class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result = 0
        for i in range(low, high+1):
            num = str(i)
            len_num = len(num)
            if len_num % 2:
                continue
            sum_left = 0
            sum_right = 0

            for j in range(len_num//2):
                sum_left += int(num[j])
            
            for j in range(len_num//2, len_num):
                sum_right += int(num[j])
            
            if sum_left == sum_right:
                result += 1
        
        return result
