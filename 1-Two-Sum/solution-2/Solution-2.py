class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}  # A dictionary to store seen elements
        for idx, val in enumerate(nums):
            complement = target - val
            if complement in num_dict:
                return [num_dict[complement], idx]
            num_dict[val] = idx  # Add the current element to the dictionary
        return []  # If no valid pair is found, return an empty list