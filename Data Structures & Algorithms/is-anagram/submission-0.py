class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) > len(t) or len(t) > len(s):
            return False

        else:
            sorted_string_1 = ''.join(sorted(s))
            sorted_string_2 = ''.join(sorted(t))

            if sorted_string_1 == sorted_string_2:
                return True
        return False
            

            
            
        