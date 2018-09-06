# 11 or 7 or 5 or 3 で割り切れる数字 range(1, 30)

def make_array(list1):
    list2 = list(filter(lambda x: x%11==0 or x%7==0 or x%5==0 or x%3==0, list1))
    return print(list2)

make_array(list(range(1, 31)))
