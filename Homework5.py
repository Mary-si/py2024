txt: str = "www.my_site.com#about"
print(txt.replace("#", "/"))

a = ["run", "go", "lie"]
for word in a:
    "{word}ing"
word_list_ing = " ".join(f"{word}ing" for word in a)
print(word_list_ing)

b = "Ivanou Ivan"
spaceIndex = b.find(" ")
word1 = b[:spaceIndex + 1]
word2 = b[spaceIndex + 1:]
print(word2 + " " + word1)

s = " Hello World! "
s = s.strip()
print(s)

txt = "pARiS"
print(txt.capitalize())
