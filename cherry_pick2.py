#自然数nを任意の数格納した配列nsと、自然数ｘを引数として、
#nsからx回、逐次的にその時点で最大のnを1減らした配列を作成する。

def cherry_pick(ns, x):
    if x > 0:
        mx = ns.index(max(ns))
        ns[mx] -= 1
        return cherry_pick(ns, x-1)
    else:
        print(ns)

cherry_pick([9, 7, 8], 3)
cherry_pick([9, 7, 8], 10)