class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.list = []
        self.olderItem = 0

    def append(self, item):
        # check the length of the list
        if len(self.list) == self.capacity:
            # if full, replace the oldest item
            if self.olderItem >= self.capacity:
                print(self.list)
                self.olderItem = 0
                self.list[self.olderItem] = item
            else:
                self.list[self.olderItem] = item

            self.olderItem += 1
        else:
            self.list.append(item)

    def get(self):
        return self.list