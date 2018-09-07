from collections import Counter


class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        _hash = Counter(p)
        _hash_len = len(p)
        result = []
        for i in range(len(s) - _hash_len + 1):
            if Counter(s[i:i + _hash_len]) == _hash:
                result.append(i)
        return result


solution = Solution()

tests = (
    (('cbaebabacd', 'abc'), [0, 6]),
    (('abab', 'ab'), [0, 1, 2]),
    (('acdcaeccde', 'c'), [1, 3, 6, 7]),
    (('beeaaedcbc', 'c'), [7, 9]),
    (('ababababab', 'aab'), [0, 2, 4, 6]),
)

for _input, expected_result in tests:
    actual_result = solution.findAnagrams(*_input)
    assert actual_result == expected_result, f'{actual_result} != {expected_result}, {_input}'
