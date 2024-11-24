class RecentCounter:

    def __init__(self):
        self.__counter = []

    def __update_queue(self, t: int):
        threshold = t - 3000
        index = 0
        while index < len(self.__counter):
            if self.__counter[index] < threshold:
                self.__counter.pop(0)
            else:
                index += 1

    def ping(self, t: int) -> int:
        self.__counter.append(t)
        self.__update_queue(t)
        return len(self.__counter)
