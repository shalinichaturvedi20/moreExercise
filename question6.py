# string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
# i=0
# b=[]
# while i<len(string_list):
#     h=0
#     while h<len(string_list):
#         if string_list[i]==string_list[h] not in b:
#             b.append(string_list[h])
#         h=h+1 
#     i=i+1
# print(b)         





string_list = ["Delhi", "Delhi", "Mumbai", "Mumbai", "Delhi", "Chennai", 'Chennai']
i=0
b=[]
while i<len(string_list):
    h=0
    while h<len(string_list):
        if string_list[i]==string_list[h] not in b:
            b.append(string_list[h])
        h=h+1 
    i=i+1
print(b)         



# s = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"] 
# i=0
# b=[]
# while i<len(s):
#     h=0
#     while h<len(s):
#         if s[i]==s[h] not in b:
#             b.append(s[h])
#         h=h+1 
#     i=i+1
# print(b)           


