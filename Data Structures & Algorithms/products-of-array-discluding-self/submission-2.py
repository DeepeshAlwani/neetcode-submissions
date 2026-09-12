class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        temp = 1
        zero_count = 0
        for i, num in enumerate(nums):
            if num == 0 :
                zero_count +=1
            else:
                temp = temp * num
        print(temp)
        for i, num in enumerate(nums):
            if zero_count > 1:
                result.append(0)
            elif zero_count != 0:
                if num == 0:
                    result.append(temp)
                else:
                    result.append(0)
            else:
                result.append(int(temp/num))

            
        return result
        