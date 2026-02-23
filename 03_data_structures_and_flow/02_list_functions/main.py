# Lists - Functions

workers_list = ["Maria", "Alex", "Robert", "Cristina", "Tina", "Markus", "Helen", "Irina"]
print("Initial list:", workers_list)

# indexing
print("Fourth item:", workers_list[3])
print("Last item:", workers_list[-1])

# add items
workers_list.append("Heinz")
print("After append:", workers_list)

workers_list.insert(3, "Paul")
print("After insert:", workers_list)

# remove items
workers_list.remove("Cristina")
print("After remove:", workers_list)

last_item = workers_list.pop()
print("Popped item:", last_item)
print("After pop:", workers_list)

# length
print("Number of items:", len(workers_list))

# check workers status
print("Is `Alex` in workers list?", "Alex" in workers_list)

# sorting
numbers = [6, 7, 2, 4, 8, 10, 6, 1]
print("\nNumbers:", numbers)

sorted_numbers = sorted(numbers)
print("sorted(numbers):", sorted_numbers)
print("numbers after sorted():", numbers)

numbers.sort()
print("numbers after sort():", numbers)

