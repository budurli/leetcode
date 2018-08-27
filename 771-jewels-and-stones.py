def numJewelsInStones(J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """
    return sum([i in J for i in S])


tests = (
    (("aA", "aAAbbbb"), 3),
    (("z", "ZZ"), 0)
)

for _input, expected_result in tests:
    actual_result = numJewelsInStones(*_input)
    assert actual_result == expected_result, f'{actual_result} != {expected_result}, {_input}'
