# two sum problem done in O(n) time

def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashdict = {}
    for i in range(len(nums)):
        if (target - nums[i]) in hashdict.keys():
            return [i, hashdict[(target - nums.pop(i))]]
        else:
            hashdict[nums[i]] = i