n = int(input())
s= str(input()).lower()
proper_s= []
count= 0
a_sum= 0

for i in range(26):
    a_sum += 97 +i

#using UNICODE sum logic, with base a=97

for char in s:
    proper_s.append(char)

proper_s= set(proper_s)

for element in proper_s:
    count += ord(element)

if count < a_sum:
    print("NO")
else:
    print("YES")