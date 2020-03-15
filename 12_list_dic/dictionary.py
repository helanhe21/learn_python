phoneNumbers = {"John":"555-1234"}
phoneNumbers["Mary"] = "555-6789"
phoneNumbers["Bob"] = "444-4321"
phoneNumbers["Jenny"] = "867-5309"
print(phoneNumbers)
print(phoneNumbers["Bob"])
print(phoneNumbers.keys())
print(phoneNumbers.values())

dictionary = {}

while True:
    cmd = input("Add or look up a word(a/l)? ")
    if cmd == "a":
        word = input("Type the word: ")
        definition = input("Type the definition: ")
        dictionary[word] = definition
        print("Word added")
    elif cmd == "l":
        word_lookup = input("Type the word you want to look up? ")
        if word_lookup in dictionary.keys():
            def_lookup = dictionary[word_lookup]
            print(def_lookup)
        else:
            print("That word isn't in the dictionary yet.")
    else:
        break