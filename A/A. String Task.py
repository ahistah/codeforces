word= str(input().lower())
vowels= "aoyeui"
result=''

for char in word:
    if char not in vowels:
        result += "." + char

print(result)