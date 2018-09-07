class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        result = [[] for i in range(len(A[0]))]
        for i, _i in enumerate(A):
            for j, _j in enumerate(A[i]):
                result[j].append(_j)
        return result


solution = Solution()

tests = (
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 4, 7], [2, 5, 8], [3, 6, 9]]),
    ([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]])
)

for _input, expected_result in tests:
    actual_result = solution.transpose(_input)
    assert actual_result == expected_result, f'{actual_result} != {expected_result}, {_input}'
