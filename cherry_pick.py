#自然数 n を任意の数格納した配列 ns と、 自然数 x を引数として、 ns から x 回、
#逐次的にその時点での最大の n を 1 減らした配列にするメソッド cherry_pick を作成してください。

#cherry_pick([9, 7, 8], 3) # => [ 7, 7, 7 ]
#cherry_pick([9, 7, 8], 10) # => [ 4, 5, 5 ]


def cherry_pick(ns, nm):
    for i in range(1, nm+1):
        mx = ns.index(max(ns))
        ns[mx] -= 1
    return print(ns)

cherry_pick([9, 7, 8], 3)
cherry_pick([9, 7, 8], 10)