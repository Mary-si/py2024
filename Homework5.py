# """Homework 5"""

string = "www.my_site.com#about"
print(string.replace("#", "/"))

a = ["run", "go", "lie"]
for word in a:
    "{word}ing"
b = " ".join(f"{word}ing" for word in a)
print(b)

string = "Ivanou Ivan"
spaceIndex = string.find(" ")
word1 = string[:spaceIndex + 1]
word2 = string[spaceIndex + 1:]
print(word2 + " " + word1)

string = " Hello World! "
s = string.strip()
print(s)

txt = "pARiS"
print(txt.capitalize())
