#1から30の整数の中で、
#3か5か7か11で割り切れる数字のみが格納された配列を作成してください。

def make_array(lists):
    array = []
    for i in lists:
        if i % 11 == 0 or i % 7 == 0 or i % 5 == 0 or i % 3 == 0 :
            array.append(i)
    return print(array)

l = list(range(1, 31))
make_array(l)
