class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointer solution with one pointer at the front and at the end
        # if the sum is less, move l, if the sum is more then move r 
        # we end when they meet 
        # [1,4,4,4,4] won't be an exepcted case because theyre's always one solution

        # Time O(n) , Space O(1)
        i = 0 
        j = len(numbers) - 1

        while i < j:
            val = numbers[i] + numbers[j]

            if val == target:
                return [i + 1, j + 1]
            elif val < target:
                i += 1
            else:
                j -= 1