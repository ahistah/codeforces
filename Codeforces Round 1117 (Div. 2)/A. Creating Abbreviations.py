t= int(input())

for i in range(t):
    n, m = list(map(int, input().split()))
    counter = n
    while counter!= 0:
        word1= str(input())
        word2= str(input())
        word1= word1.capitalize()
        word2= word2.capitalize()
        letter_word1= word1[0]
        letter_word2= word2[0]
        abbreviation = letter_word1 + letter_word2
        print(abbreviation)
        counter -= 1
