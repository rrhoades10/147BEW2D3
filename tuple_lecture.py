# TUPLES - WHAT ARE THEY
# tuple an immutable list
# When/why to use tuples?
# Managing data integrity - we cannot remove or add to a tuple
# Use cases in class - when we are sending python variables to a database
# ways to pronounce tuple
# toople - which is the correct way
# tuhple - which is the incorrect way

# declaring a tuple
empty_tuple = ()
print(empty_tuple)

# python tuple() function
another_tuple = tuple()
print(another_tuple)

# tuple with stuff in it
genres = ("Fantasy", "Mystery", "Poetry")
print(genres)
# set a tuple with a series of items separated by commas
# "Packing"
more_genres = "Fantasy", "Mystery", "Poetry"
print(more_genres)

# packing with different data types
another_packed_tuple = "Prologue", "Conflict", ["Climax", "Resolution"]
print(another_packed_tuple)

# nested tuple
nested_tuple = ("Foreword", ("Chapter 1", "Chapter 2"), "Epilogue")
print(nested_tuple)
# indexing into a tuple
print(nested_tuple[1])
# index into a tuple in a tuple
print(nested_tuple[1][0])

#                   0            1            2 last item will always be index -1
regular_tuple = ("Chapter1", "Chapter2", "Chapter3")
# list nested in a tuple   0                        1                            2
another_nested_tuple = ("Prologue", ("Conflict", ["Climax", "Resolution"]), "Afterword")
#                                   (      0                1            )      
# accessing Climax within a nested tuple and list
print(another_nested_tuple[1][1][0])

# accessing the last index
print(another_nested_tuple[-1])

# slicing tuples - taking sections or slices of the tuple
my_tuple = ("Prologue", "Adventure", "Epilogue")
print(my_tuple[0:2])
#                          0                                  1                                 2
another_nested_tuple = ("Prologue", ("Conflict", ["Climax", "Resolution", "Plot Twist"]), "Afterword")
another_slice = another_nested_tuple[0:2][1][1][0:2] # ("Prologue", ("Conflict", ["Climax", "Resolution", "Plot Twist"]))
print(another_slice)
another_slice = another_slice[1] # ("Conflict", ["Climax", "Resolution", "Plot Twist"])
print(another_slice)
another_slice = another_slice[1] # ["Climax", "Resolution", "Plot Twist"]
print(another_slice)
another_slice = another_slice[0:2] #["Climax", "Resolution"]
print(another_slice)

word = another_nested_tuple[-1]
print(word)
print(word[0])
#                                         0          1           2
historical_record = ("Medieval Era", ("Knights", "Castles", ("King", "Queen")), "Renaissance Era")
# accessing Queen
yaass_queen = historical_record[1][2][1]
print(yaass_queen)

# dictionaries in typles 0                                                  1                                                       2
enchanted_library = ("Chapter 1", {"Mythical Creatures": ["Dragon", "Unicorn"], "Legendary Places": ("Atlantis", "El Dorado")}, "Chapter 2")
# Unicorn
print(enchanted_library[1]["Mythical Creatures"][1])
# Atlantis
print(enchanted_library[1]["Legendary Places"][0])

# using list() to change our tuple
my_tuple = ("Introduction", "Conclusion")
temp_list = list(my_tuple)
temp_list.append("Epilogue")
my_tuple = tuple(temp_list)
print(my_tuple)

# trying to append to a tuple
# my_tuple.append("Glossary") AttributeError

# Unpacking a tuple
# setting variables to the tuple where each variable takes the value of each position in the tuple
#              0         1         2
my_tuple = ("Magic", "Mystery", "Myth")
# 0        1      2
genre1, genre2, genre3 = my_tuple
print(genre1) # Magic
print(genre2) # Mystery
print(genre3) # Myth

# errors when packing
# genre1, genre2, genre3, genre4 = my_tuple
# ValueError because im trying to unpack to more variables than i have items in my tuple
# genre1, genre2 = my_tuple
# ValueErros becuase i have more items in my tuple than i have variables to unpack too

# *allow a variable to hold multiple postions from a tuple
# unpack operator
# spread operator in other languages ...
my_tuple = ("Prologue", "Adventure", "Climax", "Epilogue", "Glossary")
beginning, *middle, end = my_tuple
print(beginning) #Prologue
print(middle) # ["Adventure", "Climax"]
print(end) # "Epilogue"

# using sorted() sorts the tuple but also changes it to a list
print(sorted(my_tuple))
# built in functions - len() sorted() min() max()
# build in object specific methods - .remove() .append() .pop() .sort()
# my_tuple.remove("Prologue")


# LOOPLE THROUGH SOME TUPLES
#                 0            1             2
book_titles = ("Moby Dick", "1984", "To Kill a Mockingbird")
for title in book_titles:
    print(title)

# loople by index
for i in range(len(book_titles)):
    print(i, book_titles[i])

# while loople
print(len(book_titles))
#              0                 1               2
authors = ("Herman Melville", "George Orwell", "Harper Lee")
index = 0
while index < len(authors):
    print(authors[index])
    index += 1

# Looping with enumerate
#                0                    1                      2
chapters = ("The Lighthouse", "The Ministry of Truth", "The Trial")
# index + 1     chapter 1            chapter 2            chapter 3
#     unpacking index and item in the tuple that enumerate returns
for index, chapter in enumerate(chapters):
    print(f"Chapter {index + 1}: {chapter}")
print(list(enumerate(chapters)))

# looping through nested tuples
nested_tales = (("The Dawn", "The Noon"), ("The Dusk", "The Night"))
for pair in nested_tales:
    for tale in pair:
        print(tale)

# unpack nested tuples
party_guests = (("Chris", "a very nice tuxedo"), ("Kayla", "A very neat hat"), ("Victor", "a very flattering crop top"), ("Farzin", "Really nice pants"))
for guest, ware in party_guests:
    print(f"{guest} is wearing {ware}")

# looping through nested lists in a tuple
# when we have different structures in the tuple
mixed_collection = ("Poetry", ["Sonnet", "Haiku"], "Prose")
# loops through mixed collection
for element in mixed_collection:
    # check each item in teh list (element) to see if its a list
    #              check if element is a list type
    if isinstance(element, list): #return true or false - if true loop
        # if it is we loop through that element and print its contents
        for item in element:
            print(f"List item: {item}")
    else:
        # if its not we just print the element
        print(f"Tuple Element: {element}")

name = "5"
# returns true or false if the passed in object is of the type in the second argument
print(isinstance(name, str))
# returns the type of object
print(type(name))

print(type(element) == str)

if type("Hello") == dict:
    print(True)

# dict()
# str()
# int()
# float()

historical_records = ("Ancient", {"Rome": "Republic", "Greece": "Democracy"}, "Medieval")

for element in historical_records:
    if isinstance(element, dict):
        # unpacking each tuple that is returned from element.items()
        for key, value in element.items():
            print(f"{key}: {value}")
    else:
        print(element)

cities = {"Rome": "Republic", "Greece": "Democracy"}
print(cities.items())


# tuple methods
# .count - return the number of occurrences of an item in our tuple
literary_elements = ("Irony", "Metaphor", "Irony", "Symbolism")
print(literary_elements.count("Irony")) # 2

# index() - return the position of our item in the tuple
book_chapters = ("Introduction", "Rising Action", "Climax", "Conclusion")
print(book_chapters.index("Conclusion")) # 3

# tuple concatenation
epic = ("Odyssey", "Iliad")
drama = ("Hamlet", "Othello")
literary_union = epic + drama
print(literary_union)

# combine two tuples while maintaing their structural integrity
genre_pieces = (epic, drama)
print(genre_pieces)

# defining a tuple with 1 item
one_item = (1,)
print(one_item)

one_item = (1)
print(one_item)

# tuple membership
epic = ("Odyssey", "Iliad")
if "Odyssey" in epic:
    print("We found the tale you're looking for!")

party_guests = [("Chris", "Top Hat"), ("Victor", "Suit"), ("Kayla", "Bandana"), ("Winter", "Suspenders")]
# adding a party guest to our list of tuples
# BUT the part guest may not wear something that is already being worn
party_guests = [("Chris", "Top Hat"), ("Victor", "Suit"), ("Kayla", "Bandana"), ("Winter", "Suspenders")]
def add_party_guests(guest):
    
    for person, item in party_guests:
        if guest[1] == item:
            print("Sorry, somebody is already wearing that, please come back with something more unique!")
            return party_guests
    party_guests.append(guest)
    return party_guests

print(add_party_guests(("Ryan", "Onesie")))
print(add_party_guests(("Da'Von", "Birks and Chubbies")))
print(add_party_guests(("Kayla again but cooler", "J's")))
print(add_party_guests(("Caleb", "Lipstick")))
print(add_party_guests(("Brad", "Just a trench coat ༼ つ ◕_◕ ༽つ")))
print(add_party_guests(("Tim", "Top Hat")))



    







