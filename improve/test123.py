last_names = {"Rick": "Sanchez", "Morty": "Smith",
              "Birdperson": None, "Summer": "Smith"}
i = 0
for key in last_names:
    if "Smith" == last_names[key]:
        i = i + 1
print(len(last_names))
print(i)
