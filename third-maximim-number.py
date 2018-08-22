import sys


def thirdMax(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    first = second = third = -sys.maxsize - 1

    if len(nums) == 1:
        return nums[0]

    if len(nums) == 2:
        return max(nums)

    for i in nums:
        if i > first:
            first, second, third = i, first, second

        elif first > i > second:
            second, third = i, second

        elif second > i > third:
            third = i

    return third if third != -sys.maxsize - 1 else first


tests = (
    ([3, 2, 1], 1),
    ([1, 2], 2),
    ([2, 2, 3, 1], 1),
)

for _input, expected_result in tests:
    actual_result = thirdMax(_input)
    assert actual_result == expected_result, f'{actual_result} != {expected_result}, {_input}'
