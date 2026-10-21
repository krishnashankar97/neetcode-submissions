class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) # O(1) lookups
        ans = 0

        for num in num_set:
            # Only start counting if this is the first number in a sequence
            if (num - 1) not in num_set:
                curr_num = num
                curr_streak = 1

                # Now update curr_num so the loop actually progresses
                while (curr_num + 1) in num_set:
                    curr_num += 1
                    curr_streak += 1

                ans = max(ans, curr_streak)

        return ans

