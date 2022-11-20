import jieba


def partic(p):
    lst = jieba.lcut(p)
    for i in lst:
        print(i, end=' ')
    print()
