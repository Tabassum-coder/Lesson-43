#Write a Python program to create a Python list of your favourite fruits (minimum 5). 
# Then perform the given operations on it.

fruits=["Mango","Apple","Cherry","Banana","WaterMelon"]

#length of list
print("Length of fruits list is ",len(fruits))

#indexing
print("I like ",fruits[4])

#adding values to list
fruits.append("Kiwi")

print("Updated list is ",fruits)

#removing values from list
fruits.remove("Banana")

print("Updated list after removing ",fruits)

#sorting
fruits.sort()
print("Sorted list is ",fruits)

fruits.reverse()
print("Reversed list is ",fruits)

#slicing
print("Sliced List ",fruits[1:3])