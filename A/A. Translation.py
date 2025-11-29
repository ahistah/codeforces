s= str(input())
t= str(input())
lst_s= []
lst_t= []

for char in s:
    lst_s.append(char)

for letters in t:
    lst_t.append(letters)

lst_t.reverse()

if lst_s == lst_t:
    print("YES")
else:
    print("NO")