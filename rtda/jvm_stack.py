class Stack(object):
    """栈"""

    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.__list = []

    def push(self, item):
        """添加一个新的元素item到栈顶"""
        if len(self.__list) >= self.maxSize:
            raise OverflowError
        self.__list.append(item)

    def pop(self):
        """弹出栈顶元素"""
        return self.__list.pop()

    def top(self):
        return self.__list[-1]

    def peek(self):
        """返回栈顶元素"""
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        """判断栈是否为空"""
        return self.__list == []
        # return not self.__list

    def size(self):
        """返回栈的元素个数"""
        return len(self.__list)

    def clear(self):
        self.__list = []

    def getFrames(self):
        res = [x for x in self.__list]
        res.reverse()
        return res


def newStack(num):
    return Stack(num)
