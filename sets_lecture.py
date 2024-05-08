# an mutable, unordered collection of elements that holds no duplicates
# removing duplicates from a set of data
# they're more efficient than lists, theyre hashed like dictionaries

# declaring a set 
my_set = {"Alice", "Bob", "Charlie"}
print(my_set)

# declaring empty set
my_set = set()
print(my_set)

# turning a list into a set
guest_list = ["Alice", "Bob", "Charlie"]
print(guest_list)
set_list = set(guest_list)
print(set_list)

# remove duplicates from a list with a set
guest_list = ["Alice", "Alice", "Diana", "Bob", "Bob"]
no_dupes = set(guest_list)
print(no_dupes)
guest_list = list(no_dupes)
print(guest_list)

# converting a Tuple to a set
my_tuple = ("LOTR", "LOTR", "The Hobbit", "Harry Potter")
my_set = set(my_tuple)
print(my_set)

# changing the values in a dictionary to a set
dict_guests = {"name1": "Alice", "name2": "Bob", "name3": "Alice"}
print(dict_guests.values())
set_party = set(dict_guests.values())
print(set_party)

set_dict = set(dict_guests)
print(set_dict)


# Looping through sets
guests = {"Alice", "Bob", "Charlie"}
for guest in guests:
    print(f"Welcome {guest} to the party!")


# membership checks in sets
if "Alice" in guests:
    print("Alice is enjoying the party!")
else:
    print("We didnt invite Alice, her feet smell!")

# data types in sets
# only immutables types in a set
# because the items need to be hashable in order to find their location
# no lists or dictionaries or sets in sets
test_set = {1, 2, 3, "Hello there", "Goodbye"}
print(test_set)
# set_list = {{1, 2, 3}} lists or sets in a set will cause a TypeError
print(set_list)

# set.add(thing we're adding to the set)
guests = {"Alice", "Bob", "Charlie"}
guests.add("Diana")
print(guests)
# adding someting that is already in the set
guests.add("Charlie")
print(guests)

# adding more than one item at a time
# set.update(iterable)
guests = {"Alice", "Bob", "Charlie"}
guests.update(["Linda"])
print(guests)

# set.update(iterable)
guests = {"Alice", "Bob", "Charlie"}
# remove duplicates from the iterable we're updating with
guests.update({"Linda", "Gene", "Charlie"})
print(guests)

# name = "Ryan"
# name[1] = "i" TypeError
# We can only add or remove from sets, we cannot change the shape of the contents inside
guests = {"Alice", "Bob", "Charlie"}
# remove duplicates from the iterable we're updating with
guests.update({"cool lady":"linda", "Gene": "cool guy", "Charlie": "brown"})
print(guests)
# updates with just the keys from a dictionary

# removing from a set
guests.remove("Alice")
print(guests)
# throwing an error with remove
# guests.remove("Tina") #KeyError for items that dont exist

# set.discard(thing to discard)
guests.discard("cool lady")
print(guests)
# trying to discard someone that doesnt exist
guests.discard("Teddy")
print(guests)

# set.pop()
guests = {"Alice", "Bob", "Charlie"}
random_guest = guests.pop()
print(f"We're at capacity. We have to ask {random_guest} to leave.")

our_class = {"Winter", "Farzin", "Victor", "Kayla", "Spencer", "Brad", "Chris", "Karen", "Andy", "Da'Von", "Pheona", "Taylor", "Caleb"}
random_person = our_class.pop()
print(f"{random_person} has to do an impromptu whiteboard")
print(our_class)
print(len(our_class))

# set.union(set2)
# merge two sets together
# order of sets we're calling does not matter
set1 = {"Alice", "Bob", "Charlie"}
set2 = {"David", "Emma", "Charlie"}
new_set = set1.union(set2)
print(new_set)

# Intersection
# find the commonality between two sets
# which items are the same
# order of sets doesnt matter
set1 = {"Alice", "Bob", "Charlie"}
set2 = {"David", "Emma", "Charlie", "bob"}
mutual_friends = set1.intersection(set2)
print(mutual_friends)

# Difference
# what is in set1 that is not in set2 
# order of sets matters
set1 = {"Alice", "Bob", "Charlie"}
set2 = {"David", "Emma", "Charlie"}

# unique to set1
exclusive_guests = set1.difference(set2)
print(exclusive_guests)
# unique to set2
exclusive_guests = set2.difference(set1)
print(exclusive_guests)

# Symmetric Difference
set1 = {"Alice", "Bob", "Charlie"}
set2 = {"Charlie", "David", "Emma"}
unique_attendees = set1.symmetric_difference(set2)
print(unique_attendees)

# enumerate with sets
guests = {"Zoob", "Bob", "Charlie", "Alice"}
for index, guest in enumerate(guests):
    print(f"Guest #{index} is {guest}")

# sorted = turn the set into a list and then sort its contents
guests = {"Zoob", "Bob", "Charlie", "Alice"}
print(sorted(guests))
for index, guest in enumerate(sorted(guests)):
    print(f"Guest #{index + 1} is {guest}")


# set comprehension
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# transform(thing we're adding) for loop conditional
odd_square_party = {num**2 for num in range(10) }
empty_set = set()
# empty_set = {} <-- thinks this is a dictionary
print(odd_square_party)
# for num in nums:
#     if num % 2 != 0:
#         empty_set.add(num**2)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# transform(thing we're adding) for loop conditional
even_square_party = [num**2 for num in nums if num % 2 == 0]
print(even_square_party)
# for num in nums:
#     if num % 2 == 0:
#         even_square_party.append(num**2)



nums = [1, 2, 3,3,3,3,3,3,3, 4, 5, 6, 7,7,7,7,7,7,7,7,7, 8, 9,9,9,9,9,9,9, 10, 11, 12, 13,13,13,13,13,13,13, 14, 15]
print(len(nums))
set_nums = set(nums)
print(len(set_nums))
for num in nums:
    if num % 2 == 0:
        print("even")

guests = ["Alice", "Bob", "Charlie"]
guest_list = {"Alice", "Bob", "Charlie"}

for name in guests:
    if name == "Alice":
        print("alice is here")