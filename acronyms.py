user_input = input("-> ")
phrase = (user_input.replace('of','')).replace('and','').split()
acronym = ""
for word in phrase:
    acronym = acronym + word[0].upper()
print(acronym)