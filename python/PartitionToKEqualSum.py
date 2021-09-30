# Question No. 698
# Partition to K Equal Sum Subsets
class Solution:
    def canPartitionKSubsets(self, nums, k: int) -> bool:
        self.divide, rem = divmod(sum(nums), k)
        nums.sort(reverse = True)
        # Sort is actually very crucial for pruning
        self.numbers = nums
        self.N = len(self.numbers)
        self.bucket_len = k
        if rem or nums[0] > self.divide:
            return False
        buckets = [0] * k
        buckets[0] = nums[0]
        return self.solvePartition(1, buckets)
        
    def find_valid_spot(self, index, buckets):
        results = []
        value_set = set()
        for i in range(self.bucket_len):
            if buckets[i] not in value_set and buckets[i] + self.numbers[index] <= self.divide:
                results.append(i)
                value_set.add(buckets[i])
        return results
    
    def solvePartition(self, index, buckets):
        if index >= self.N:
            return True
        valid_spots = self.find_valid_spot(index, buckets)
        if len(valid_spots) == 0:
            return False

        for spot in valid_spots:
            bucket_copy = buckets.copy()
            bucket_copy[spot] += self.numbers[index]
            if self.solvePartition(index + 1, bucket_copy):
                return True