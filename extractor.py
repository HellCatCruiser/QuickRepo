"""
This code extracts the attributes and their types
"""

lines = []

f = open("form Leerlingen.txt")
list1 = (f.readlines())
# print(len(list1))
for i in range(0, len(list1)):
    if "(" not in list1[i] and ")" not in list1[i] and "{" not in list1[i] and "}" not in list1[i] and "row" not in list1[i] and "column" not in list1[i] and "width" not in list1[i] and "field alignment" not in list1[i] and "feature property" not in list1[i] and "displayname" not in list1[i] and "alloweddays" not in list1[i] and "initial value" not in list1[i] and "visibility" not in list1[i] and "maxchar" not in list1[i] and "values" not in list1[i] and "height" not in list1[i] and "toolbar" not in list1[i] and "[" not in list1[i]and "]" not in list1[i] and "personal data" not in list1[i] and "sortorder" not in list1[i] and "searchable" not in list1[i] and "form Leerlingen" not in list[i] and "hide" not in list[i] and "Section" not in list[i]:
        lines.append(list1[i])
        # print(list1[i])
lines2 = ([s.strip('\n') for s in lines])
lines3 = ([s.strip("\t") for s in lines2])
lines4 = ([s.replace("\ttype", "type") for s in lines3])
lines5 = ([s.replace("\t", "") for s in lines4])
# print(lines5)
lines6 = [i.lower() for i in lines5]
# print(lines6)
lines7 = []
for i in lines6:
    if 'form leerlingen' not in i and "success message" not in i and "section" not in i and "hide" not in i:
        lines7.append(i)
# print(lines7)
lines8 = ([s.replace('must have', '') for s in lines7])
print(lines8)

with open('attributes.txt', 'w') as outfile:
  outfile.write('\n'.join(str(i) for i in lines8))




# x = lines[2]
# print(x)