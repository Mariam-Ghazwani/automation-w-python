x = ["Now", "we", "are", "cooking!"]
type (x)
print(x)
len(x)
print(x[0])
print(x[3])


def group_list(group, users):
  members = group + ": " + ", ".join(users)
  return members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"

# Modifying the Contents of a List
fruits.append("Kiwi")
fruits.insert(0,"Orange")
fruits.remove("Melon")
fruits.pop(3)
# to modify/change/replace the element in the list
fruits[2] = "Strawberry"
