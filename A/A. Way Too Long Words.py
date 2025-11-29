def abbreviation():
    print(word[0] + str(length-1) + word[length])

n= int(input())

for i in range(n):
    word = str(input())
    length = len(word) - 1
    if length > 9:
        abbreviation()
    else:
        print(word)


