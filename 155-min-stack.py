class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self._stack_len = 0
        self._min = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self._min is None or x < self._min:
            self._min = x
        self._stack_len += 1
        self._stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self._stack_len == 0:
            return None

        _pop = self._stack.pop()
        self._stack_len -= 1

        if self._stack_len == 0:
            self._min = None
        elif _pop == self._min:
            self._min = min(self._stack)

        return _pop

    def top(self):
        """
        :rtype: int
        """
        if self._stack_len == 0:
            return None
        return self._stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self._stack_len == 0:
            return None
        return self._min


minStack = MinStack()
minStack.push(0)
minStack.push(1)
minStack.push(2)
assert minStack.getMin() == 0
