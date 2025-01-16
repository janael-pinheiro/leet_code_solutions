class MinStack:
    def __init__(self):
        self.__internal_stack = []
        self.__minimum_stack = []
        self.__current_minimum = 2 ** 32
        self.__top_element = None

    def push(self, val: int) -> None:
        self.__internal_stack.insert(0, val)
        self.__top_element = val
        if val <= self.__current_minimum:
            self.__current_minimum = val
            self.__minimum_stack.insert(0, val)

    def pop(self) -> None:
        current = self.__internal_stack.pop(0)
        if len(self.__internal_stack) > 0:
            top_element = self.__internal_stack.pop(0)
            self.__internal_stack.insert(0, top_element)
            self.__top_element = top_element
        current_minimum = self.__minimum_stack.pop(0)
        if current != current_minimum:
            self.__minimum_stack.insert(0, current_minimum)
        else:
            if len(self.__minimum_stack) > 0:
                current_minimum = self.__minimum_stack.pop(0)
                self.__current_minimum = current_minimum
                self.__minimum_stack.insert(0, current_minimum)
            else:
                self.__current_minimum = 2 ** 32

    def top(self) -> int:
        return self.__top_element

    def getMin(self) -> int:
        return self.__current_minimum
