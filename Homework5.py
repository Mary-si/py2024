# """Homework 5"""

site = "www.my_site.com#about"
print(site.replace("#", "/"))

word_list = ["run", "go", "lie"]
for word in word_list:
    "{word}ing"
word_ing = " ".join(f"{word}ing" for word in word_list)
print(word_ing)

string = "Ivanou Ivan"
spaceIndex = string.find(" ")
last_name = string[:spaceIndex + 1]
first_name = string[spaceIndex + 1:]
print(first_name + " " + last_name)

txt = " Hello World! "
s = txt.strip()
print(s)

txt = "pARiS"
print(txt.capitalize())
