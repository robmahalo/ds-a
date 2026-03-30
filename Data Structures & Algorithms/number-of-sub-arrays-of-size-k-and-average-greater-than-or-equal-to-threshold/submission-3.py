# use sliding window
# start = 0, state = 0, count = 0
# loop through nums
# if end - start > k, 
# state / k, if state >= threshold, count += 1,
# remove start, start += 1
# state += nums[end]

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        start = 0
        state = 0
        count = 0

        for end in range(len(arr)):
            state += arr[end]

            if end - start + 1 == k:
                if state / k >= threshold:
                    count += 1
                state -= arr[start]
                start += 1
                
        return count


        