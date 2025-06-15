class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Working solution 
        # Time Complexity O(n log n)
        # Space Complexity O(sort)
        # arr = sorted(citations, reverse=True)
        # cnt = 0
        # for i in range(len(arr)):
        #     if arr[i] >= i + 1:
        #         cnt += 1
        # return cnt
        n = len(citations)
        bkt = [0] * (n + 1) # the change here would be to add an extra bkt 
        # because there could be a case where it's the literal length that's the answer

        # for i in range(len(citations)):
        #     if citations[i] >= len(bkt):
        #         bkt[-1] += 1
        #     else:
        #         bkt[citations[i]] += 1

        # a more simplified approach to putting it last or just putting it where it is
        for c in citations:
            if c >= n:
                bkt[n] += 1
            else:
                bkt[c] += 1
        
        cnt = 0
        for idx in range(n, -1, -1): # the case for the length that's why we got rid of the -1 here
            cnt += bkt[idx]
            if cnt >= idx:
                return idx
        return 0
        
        # What we did here was
        # reduce the the time to just O(n)

        # We made it where we made buckets to count how many papers 
        # existed that had that many citations
        # we then utilized that array to go backwards and determine
        # if that overarching count is greater than the citation idx
        # once that's true we return the idx which represents 
        # the amount of citations