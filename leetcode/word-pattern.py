class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
    #     You would solve this by splitting s into an arr we would 
    #     then do a two pointer system where we would check that 
    #     of the pattern and s and compare that to the mapping and 
    #     defined to determine if its valid 
        mapping = {}
        defined = set()
        arr = s.split(' ')
        if len(pattern) != len(arr):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in mapping and arr[i] not in defined:
                mapping[pattern[i]] = arr[i]
                defined.add(arr[i])
            elif pattern[i] in mapping and arr[i] in defined:
                if mapping[pattern[i]] == arr[i]:
                    continue
                return False
            else:
                return False

        return True