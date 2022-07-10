import string 
s1 = string.ascii_lowercase
s2 = string .ascii_uppercase
k = 98%26
s_new =''
s = '159357lcfd'
s = list(s)
s1_change = s1[k:] + s1[:k]
s2_change = s2[k:] + s2[:k]
print(len(s1))
print(s1_change)

for k in range(len(s)): 
    for i,j in enumerate(s1):
        if s[k] == j: 
            s[k] = s1_change[i]
            break
    for i,j in enumerate(s2):
        if s[k] == j: 
            s[k] = s2_change[i]            
            break
for i in s: 
    s_new +=i
print(s_new)