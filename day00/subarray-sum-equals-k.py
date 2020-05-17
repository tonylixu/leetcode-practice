class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # We will construct an additional dictionary to keep the sum of
        # all the elements before the index, for example
        # given nums = [1, 4, 0, 3, 2]
        # the element sum list: sum_list = [0, 1, 5, 5, 8, 10]
        # Then we turn the sum_list into a dictionary
        # sum_dict = {
        #    0: 1
        #    1: 1
        #    5: 2
        #    8: 1
        #    10: 1
        # }
        # The key of the sum_dict stands for the sum
        # The value of the key would be the number of substrings to
        # get to this value
        # Time complexity: O(n)
        # Space complexity: O(2n) = O(n)
        sum_dict = {0: 1}
        count = s = 0

        # Iterate nums
        for n in nums:
            s += n
            # Check if "k" can be formed by "n" and previous sums: "s-k"
            count += sum_dict.get(s - k, 0)
            # Add new sum into the dictionary
            if s in sum_dict:
                sum_dict[s] += 1
            else:
                sum_dict[s] = 1
        return count
