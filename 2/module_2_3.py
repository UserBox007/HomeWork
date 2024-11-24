my_list =  [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
x = 0
l = len(my_list) - 1
while x < l :
    val_ = my_list[x]
    if val_ == 0 :
        x += 1
        continue
    if val_ <  0 :
        break
    print(val_)
    x+=1
