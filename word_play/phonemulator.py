import itertools
import random

with open("consonants.txt", "r") as consonants_file:
    consonants = consonants_file.read().split("\n")
with open("vowels.txt", "r") as vowels_file:
    vowels = vowels_file.read().split("\n")

products = []
list_products = []
random_products = []
i = 1
products.append(itertools.product(consonants, vowels, repeat=i))
products.append(itertools.product(vowels, consonants, repeat=i))
products.append(itertools.product(consonants, vowels, consonants, repeat=i))
for index in (0, 1, 2):
    list_products += ["".join(word) for word in products[index]]

for word in list_products:
    if random.randint(0, 100000) > 99999:
        random_products += [word]

for i in range(10):
    print(random.choices(list_products)[0], random.choices(list_products)[0])
print("hello?")