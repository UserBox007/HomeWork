def get_password(key):
    result = ""

    if(key < 3):
        return result

    i = 1
    while i < key:
        j = i
        while j < key:
            if i == j:
                j += 1
                continue
            if key % (i+j) == 0:
                result += str(i)+str(j)
            j+=1
        i+=1
    return  result


key = 3
while key < 21:
    print(key, get_password(key))
    key += 1