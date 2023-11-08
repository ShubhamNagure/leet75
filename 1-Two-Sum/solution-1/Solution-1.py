class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result=[]
        for idx, valx in enumerate(nums):
            for idy, valy in enumerate(nums):
                if idx != idy and valx+valy == target:
                    # if not idx in result and not idy in result:
                    result.append(idx)
                    result.append(idy)
        return result[:2]
