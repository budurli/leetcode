def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    raise NotImplementedError


tests = (
    (["flower", "flow", "flight"], 'fl'),
    (["dog", "racecar", "car"], '')
)

for _input, expected_result in tests:
    actual_result = longestCommonPrefix(_input)
    assert actual_result == expected_result, f'{actual_result} != {expected_result}, {_input}'
