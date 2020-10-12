class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.size = k
        # initialize queue with none
        self.queue = [None for i in range(k)]
        self.front = self.rear = -1

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        # if queue is full
        if (self.rear + 1) % self.size == self.front:
            print(self.rear, self.front)
            return False
        self.rear += 1
        self.rear = self.rear % self.size
        self.queue[self.rear] = value
        # if queue was empty, set front to rear
        if self.queue[self.front] == None:
            self.front = self.rear
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.queue[self.front] == None:
            return False
        else:
            self.queue[self.front] = None
            self.front += 1
            self.front = self.front % self.size
            return True


    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.queue[self.front] == None:
            return -1
        else:
            return self.queue[self.front]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.queue[self.rear] == None:
            return -1
        else:
            return self.queue[self.rear]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if self.queue[self.front] == None:
            return True
        else:
            return False

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if (self.rear + 1) % self.size == self.front:
            return True
        else:
            return False


if __name__ == '__main__':

    # Your MyCircularQueue object will be instantiated and called as such:
    obj = MyCircularQueue(3)
    print(obj.enQueue(1))
    print(obj.deQueue())
    print(obj.enQueue(1))

    # print(obj.enQueue(2))
    # print(obj.enQueue(3))
    # print(obj.enQueue(4))
    print(obj.Rear())
    print(obj.isFull())
    print(obj.enQueue(4))
    print(obj.rear)
