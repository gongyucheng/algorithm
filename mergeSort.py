def merge(a, b):
    c = []
    h = j = 0
    #print('c1111===', c)
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)

    print('合并归=====',c)
    return c


def merge_sort(lists):
    print('sort函数===',lists)
    if len(lists) <= 1:
        print('sort结束--')
        return lists
    middle = len(lists)//2
    left = merge_sort(lists[:middle])
    print('左边======', left)
    right = merge_sort(lists[middle:])
    print('右边======', right)
    #print('left===',left,right)
    return merge(left, right)


if __name__ == '__main__':
    a = [4, 7, 8, 3, 5, 9]
    print(merge_sort(a))