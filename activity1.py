#Write a Python program to create a Python list of your favourite fruits (minimum 5). Then perform the given operations on it

list1=['orange','banana','apple','cherry','kiwi']

print("List elements are ",list1)

#indexing
print(list1[2]," is rich in iron ")

#slicing
print("Sliced list is ",list1[1:4])

#append
list1.append('watermelon')
print("Updated list after adding is ",list1)

list1.sort()
print("Sorted list is ",list1)

list1.reverse()
print("Reversed list is ",list1)

#remove
list1.remove('cherry')
print("Updated list after removing is ",list1)

#pop
list1.pop(3)
print("List after popping an element is ",list1)

print("Length of the list is ",len(list1))

list1.clear()
print(list1)