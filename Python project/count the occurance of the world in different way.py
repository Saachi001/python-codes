# it will search in three format ; as given, lower case, upper case.
strl = input("String to search in: ")
word_to_search = input("Word to search: ")
as_given = strl.count(word_to_search)
lower_count = strl.count(word_to_search.lower())
upper_count = strl.count(word_to_search.upper())
print("count")
print("as_given:", as_given)
print("Lowercase:", lower_count)
print("Uppercase:", upper_count)