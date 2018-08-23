def reverseBits(n):
    """
    :type n: int
    :rtype int
    """
    return int('{:032b}'.format(n)[::-1], 2)


tests = (
    (43261596, 964176192),
)

for _input, expected_result in tests:
    actual_result = reverseBits(_input)
    assert actual_result == expected_result, f'{actual_result} != {expected_result}, {_input}'
