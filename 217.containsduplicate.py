# date completed: 2 July 2023

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        new_dict = dict()

        for num in nums:
            if num not in new_dict:
                new_dict[num] = 1
            else:
                new_dict[num] += 1

        print(new_dict)
        for key, value in new_dict.items():
            print(value)
            if value is not 1:
                return True
