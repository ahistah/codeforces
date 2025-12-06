testCases= int(input())

for _ in range(testCases):
    n= int(input())
    colors= list(map(int, input().split()))
    setColors= set(colors)
    normalizedColors= list(setColors)
    distinctElements = len(normalizedColors)
    normalizedColors.sort()
    for element in normalizedColors:
        if element >= distinctElements:
            print(element) 
            break
