s1= str(input())
s2= str(input())
s3= ''

a1=[]
a2=[]
a3=[]

for char in s1:
    a1.append(char)

for char in s2:
    a2.append(char)

for i in range(len(a1)):
    if a1[i] != a2[i]:
        a3.append('1')
    else:
        a3.append('0')

s3=''.join(a3)

print(s3)

#this is basically a manual python xor