letters= str(input()).strip('{}').split(', ')

elements= len(set(letters))
if letters[0] == '':
    print(0)
else:
    print(elements)

