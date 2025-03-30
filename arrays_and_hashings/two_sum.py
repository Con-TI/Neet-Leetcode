class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict({})
        for i, num in enumerate(nums):
            complement = target - num
            if hash_map.get(complement) == None:
                hash_map[num] = i
            else:
                return [hash_map.get(complement),i]
        return False