#QUESTION NO 1:

# original string
x = "123"
print("x:", x)
print("Type of x:", type(x))

# cast to integer
y = int(x)
print("y (as integer):", y)
print("Type of y:", type(y))

# cast to float
z = float(x)
print("z (as float):", z)
print("Type of z:", type(z))

# cast integer to string
num = 456
num_str = str(num)
print("num_str (as string):", num_str)
print("Type of num_str:", type(num_string)
      
#QUESTION NO 2:      
# 1. Access items in a list
my_list = [10, 20, 30, 40, 50]
print("First item:", my_list[0])
print("Last item:", my_list[-1])

# 2. Use loops with lists
for item in my_list:
    print("Item:", item)

# 3. Add items to a list
my_list.append(60)
print("After append:", my_list)
my_list.insert(2, 25)
print("After insert at index 2:", my_list)

# 4. Remove items from a list
my_list.remove(30)
print("After removing 30:", my_list)
popped_item = my_list.pop()
print("Popped item:", popped_item)
print("After pop:", my_list)

# 5. Sort a list
numbers = [4, 2, 9, 1, 7]
numbers.sort()
print("Sorted list:", numbers)
numbers.sort(reverse=True)
print("Sorted in reverse:", numbers)

# 6. Copy a list
copy_list = my_list.copy()
print("Original list:", my_list)
print("Copied list:", copy_list)

# 7. Use list comprehension
squared = [x ** 2 for x in numbers]
print("Squares of numbers:", squared)

#QUESTION NO 3:
# define a tuple
my_tuple = (10, 20, 30, 40, 50)

# 1. Accessing tuple items
print("First item:", my_tuple[0])
print("Last item:", my_tuple[-1])

# 2. Looping through a tuple
for item in my_tuple:
    print("Item:", item)

# 3. Joining tuples
tuple2 = (60, 70)
joined_tuple = my_tuple + tuple2
print("Joined tuple:", joined_tuple)

# 4. Updating a tuple (create a new one because tuples are immutable)
temp_list = list(my_tuple)
temp_list[1] = 25
updated_tuple = tuple(temp_list)
print("Updated tuple:", updated_tuple)

# 5. Unpacking a tuple
a, b, c, d, e = my_tuple
print("Unpacked values:", a, b, c, d, e)

# 6. Tuple methods
count_20 = my_tuple.count(20)
index_30 = my_tuple.index(30)
print("Count of 20:", count_20)
print("Index of 30:", index_30)
 
 #QUESTION NO 4:
 # Define a set
my_set = {1, 2, 3, 4, 5}

# Add an item
my_set.add(6)
print("After add:", my_set)

# Update set with multiple items
my_set.update([7, 8, 9])
print("After update:", my_set)

# Remove an item
my_set.remove(3)
print("After remove 3:", my_set)

# Discard an item (no error if not found)
my_set.discard(10)
print("After discard 10 (not in set):", my_set)

# Pop an item (removes a random item)
popped_item = my_set.pop()
print("Popped item:", popped_item)
print("After pop:", my_set)

# Clear the set (remove all items)
copy_set = my_set.copy()
copy_set.clear()
print("Cleared copy_set:", copy_set)

# Set union
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a.union(set_b)
print("Union of set_a and set_b:", union_set)

# Set intersection
intersection_set = set_a.intersection(set_b)
print("Intersection of set_a and set_b:", intersection_set)

# Set difference
difference_set = set_a.difference(set_b)
print("Difference of set_a and set_b (set_a - set_b):", difference_set)
 
 #QUESTION NO 5:
 import array

# Create an array of integers
my_array = array.array('i', [1, 2, 3, 4, 5])
print("Array:", my_array)

# Access array items
print("First item:", my_array[0])
print("Last item:", my_array[-1])

# Add items to array
my_array.append(6)
print("After append:", my_array)

# Insert item at position
my_array.insert(2, 99)
print("After insert at index 2:", my_array)

# Remove item
my_array.remove(3)
print("After remove 3:", my_array)

# Pop item
popped = my_array.pop()
print("Popped item:", popped)
print("After pop:", my_array)

# Loop through array
for item in my_array:
    print("Item:", item)

# Compare with list
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)

# Compare with tuple
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)

# Compare with set
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)

#QUESTION NO 6

shopping_list = ["milk", "bread", "eggs", "butter", "juice", "sugar", "salt", "biscuits", "tea", "coffee"]

# 1. Display all items using a loop
print("Shopping List:")
for item in shopping_list:
    print(item)

# 2. Ask the user if they want to add a new item
add_item = input("Do you want to add a new item? (yes/no): ")
if add_item.lower() == "yes":
    new_item = input("Enter the item to add: ")
    shopping_list.append(new_item)

# 3. Ask the user if they want to remove any item
remove_item = input("Do you want to remove any item? (yes/no): ")
if remove_item.lower() == "yes":
    item_to_remove = input("Enter the item to remove: ")
    if item_to_remove in shopping_list:
        shopping_list.remove(item_to_remove)
    else:
        print("Item not found")

# 4. Finally, display the updated list
print("Updated Shopping List:")
for item in shopping_list:
    print(item)

#QUESTION NO 7
def check_even_odd(number):
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

num = int(input("Enter a number: "))
check_even_odd(num)


#QUESTION NO 8
import math

number = 16

square_root = math.sqrt(number)
print("Square root of", number, "is:", square_root)

rounded_value = math.ceil(4.3)
print("Ceiling of 4.3 is:", rounded_value)

power_value = math.pow(2, 3)
print("2 raised to the power 3 is:", power_value)

#QUESTION NO 9
numbers = [5, 12, 7, 18, 9, 24, 3, 16, 11]

divisible_by_3 = 0
even_not_3 = 0
odd_not_3 = 0

for num in numbers:
    if num % 3 == 0:
        print(f"{num} is divisible by 3")
        divisible_by_3 += 1
    elif num % 2 == 0:
        print(f"{num} is even but not divisible by 3")
        even_not_3 += 1
    else:
        print(f"{num} is odd and not divisible by 3")
        odd_not_3 += 1

print("Total numbers divisible by 3:", divisible_by_3)
print("Total even numbers (not divisible by 3):", even_not_3)
print("Total odd numbers (not divisible by 3):", odd_not_3)

#QUESTIION NO 10
marks = (65, 70, 75, 80, 85)

print("First element:", marks[0])
print("Last element:", marks[-1])

m1, m2, m3, m4, m5 = marks
print("Unpacked values:", m1, m2, m3, m4, m5)

new_marks = (m1 + 5, m2 + 5, m3 + 5, m4 + 5, m5 + 5)

print("Original tuple:", marks)
print("New tuple (with +5 added):", new_marks)

# QUESTION NO 11
def classify_numbers(numbers):
    counts = {"positive": 0, "zero": 0, "negative": 0}
    
    for num in numbers:
        if num > 0:
            print(f"{num} is positive")
            counts["positive"] += 1
        elif num == 0:
            print(f"{num} is zero")
            counts["zero"] += 1
        else:
            print(f"{num} is negative")
            counts["negative"] += 1
    
    return counts

nums = [10, -5, 0, 7, -3, 0, 2]
result = classify_numbers(nums)

print("Counts:", result)
