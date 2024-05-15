# """Homework 5"""

site = "www.my_site.com#about"
print(site.replace("#", "/"))

words = ["run", "go", "lie"]
for word in words:
    "{word}ing"
word_ing = " ".join(f"{word}ing" for word in words)
print(word_ing)

login: str = "Ivanou Ivan"
spaceIndex = login.find(" ")
surname = login[:spaceIndex + 1]
first_name = login[spaceIndex + 1:]
print(first_name + " " + surname)

txt = " Hello World! "
s = txt.strip()
print(s)

txt = "pARiS"
print(txt.capitalize())
