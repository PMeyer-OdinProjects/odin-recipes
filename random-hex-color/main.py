import random

char = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']

color = []

for i in range(0, 6):
    i = random.choice(char)
    color.append(i)
color_hex = "".join(str(e) for e in color)
print(f"#{color_hex}")