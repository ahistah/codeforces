s= list(input().split('+'))

def linear_sort(list):
    buffer=''
    string=''
    length = len(list)
    for j in range(length-1):
        for i in range(length-j-1):
            if list[i] > list[i+1]:
                buffer = list[i] 
                list[i] = list[i+1]
                list[i+1] = buffer
    return "+".join(list)

print(linear_sort(s))