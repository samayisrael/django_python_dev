class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashset = {}

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hashset[key] = key

        self.hashset.update

    def remove(self, key: int) -> None:
        if self.contains(key):
            #delete
            del self.hashset[key]


    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        try:
            x = self.hashset[key]
        except:
            return False
        else:
            return True


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
