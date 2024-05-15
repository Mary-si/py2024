txt = "www.my_site.com#about"
print(txt.replace("#", "/"))

a = ["run", "go", "lie"]
for word in a:
    "{word}ing"
b = " ".join(f"{word}ing" for word in a)
print(b)

b = "Ivanou Ivan"
spaceIndex = b.find(" ")
word1 = b[:spaceIndex + 1]
word2 = b[spaceIndex + 1:]
print(word2 + " " + word1)

s = " Hello World! "
s = s.strip()
print(s)

a = "pARiS"
print(a.capitalize())
