class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        self.data.append(num)

    def findMedian(self) -> float:
        self.data.sort()
        n = len(self.data)
        if n % 2 != 0:
            # If n is odd, return the exact middle element
            middle_index = n // 2
            return self.data[middle_index]
        else:
            # If n is even, average the two middle elements
            right_middle_index = n // 2
            left_middle_index = (n // 2) - 1
            
            return (self.data[left_middle_index] + self.data[right_middle_index]) / 2
        