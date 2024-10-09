
from unordered_list import Unordered_List
from node import Node

my_list1 = Unordered_List()
my_list1.add_item(10)
my_list1.add_item(20)
my_list1.append_item(30)

print(my_list1)  # Output: [20, 10, 30]

my_list1.insert_item(1, 15)
print(my_list1)  # Output: [20, 15, 10, 30]

my_list1.insert_item(0, 5)
print(my_list1)  # Output: [5, 20, 15, 10, 30]

my_list1.insert_item(4, 25)
print(my_list1)  # Output: [5, 20, 15, 10, 25, 30]