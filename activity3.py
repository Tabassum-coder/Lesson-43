#Write a program to create a List with five students' details (roll no, name, grade).
#  Then convert that list into a dictionary.

def converttodict(lst):
    result_dict={}
    for item in lst:
        result_dict[item[0]]=item[1:]
    return result_dict

students=[[1,'Ali',1],[2,'Ayat',4],[3,'Yusra',2],[4,'Arham',5],[5,'Reeshan',9]]

print("Original list is ",students)

print("Converted dictionary is ",converttodict(students))