#Takes a target number and list of numbers
#Returns two of the numbers that equal the target

class Solution(object):
    def twoSum(nums, target):
        for index, n in enumerate(nums):
            number = n
            number_index = index
            print('number', n)
            for index,n in enumerate(nums):
                print('other', n)
                if index == number_index:
                    pass
                elif n+number == target:
                    return number_index, index