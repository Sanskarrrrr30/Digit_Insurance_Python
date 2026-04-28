
colors = ["red", "green", "blue", "yellow", "purple"]
print("Original list:", colors)
new_colors = []
indices_to_remove = [1, 3]

for index,color in enumerate(colors):
    print(index, color)
    if index not in indices_to_remove:
        new_colors.append(color)

print("New list after removing elements:", new_colors)