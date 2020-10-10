
from my_hashset import MyHashSet

my_test_hashset = MyHashSet()
my_test_hashset.add(1)
my_test_hashset.add(2)
my_test_hashset.remove(1)
x = my_test_hashset.contains(1)
y = my_test_hashset.contains(2)

print(x,y)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
