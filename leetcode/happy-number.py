class Solution:
    def isHappy(self, n: int) -> bool:
        # if it hits a cycle meaning we return back to the number
        # then we just return false
        aggSum = 0
        sums = set()
        val = str(n)

        while True:
            for num in val:
                aggSum += int(num) * int(num)

            if aggSum in sums:
                return False
            else:
                sums.add(aggSum)

            if aggSum == 1:
                return True
            else:
                val = str(aggSum)
                aggSum = 0

            # aggSum = n

        
        return False