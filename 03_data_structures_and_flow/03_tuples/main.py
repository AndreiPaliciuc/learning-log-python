# Tuples - basics

# A tuple is an ordered collection like a list,
# but it is IMMUTABLE (you cannot change its elements)

coordinates = (6, 10, 26, 38, 55, 11)
print("Coordinates:", coordinates)
print("X:", coordinates[0])
print("Y:", coordinates[-1])

person = ("Andrei", 24, "Germany")
print("\nPerson:", person)
print("Name:", person[0])
print("Age:", person[1])
print("Country:", person[2])

# Tuple packing / unpacking
location = ("Chemnitz", "Saxony")
city, state = location
print("\nUnpacking:")
print("City:", city)
print("State:", state)

# Typical use case: fixed values that should change
days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
print("\nDays:", days)
print("First day:", days[0])
print("Last day:", days[-1])

# Convert list <-> tuple
colors_list = ["purple", "pink", "blue", "yellow", "red"]
colors_tuple = tuple(colors_list)
print("\nList -> Tuple:", colors_tuple)

back_to_list = list(colors_tuple)
back_to_list.append("gray")
print("Tuple -> List + append:", back_to_list)

# Important: tuples cannot be modified directly
# coordinates[0] = # TypeError