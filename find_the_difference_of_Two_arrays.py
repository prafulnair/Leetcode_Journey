
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ones = set(nums1)
        twos = set(nums2)
        
        differences1 = ones - twos 
        differences2 = twos - ones
        
        answer = [list(differences1), list(differences2)]
        
        return answer