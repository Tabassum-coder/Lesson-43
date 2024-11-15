
mydict={'name':'Ali','age':6}

print(mydict)

#adding values
mydict['grade']=1

print("Updated dictionary is ",mydict)

print(mydict.get('name')," studies in grade ",mydict.get('grade'))

#removing values
mydict.pop('age')

print("Updated didctionary after removal is ",mydict)

#update value of dictionary
mydict['name']="Ayat"

print("Updated dictionary is ",mydict)