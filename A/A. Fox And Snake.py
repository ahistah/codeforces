n, m = list(map(int, input().split()))

hashtag= ""
left_hash= "#" 
right_hash= ""
step = 0

for _ in range(m):
    hashtag += "#"

for _ in range(m-1):
    left_hash += "."
    right_hash += "."

right_hash += "#"

for i in range(n//2):
    print(hashtag)
    if step%2 == 0:
        print(right_hash)
        step+=1
    else:
        print(left_hash)
        step+=1

print(hashtag)