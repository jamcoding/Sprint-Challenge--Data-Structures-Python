class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.list = []
        self.oldestItem = 0

    def append(self, item):
        # checking the length
        if len(self.list) == self.capacity:
            # if full, replace the oldest item
            if self.oldestItem >= self.capacity:
                print(self.list)
                self.oldestItem = 0
                self.list[self.oldestItem] = item
            else:
                self.list[self.oldestItem] = item

            self.oldestItem += 1
        # else - append item to list
        else:
            self.list.append(item)

    def get(self):
        return self.list