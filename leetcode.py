from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    # hash map to store vaules and their indices
    num_map = {}
    
    for index, num in enumerate(nums):
        complement = target - num
        
        if complement in num_map:
            # Return the index of the complement and the current index
            return [num_map[complement], index]
        
        # store the current number and its index in the hash map
        num_map[num] = index
        
print(twoSum(any, [2,7,11,15], 9)) # Example usage