import sys

sys.setrecursionlimit(1000000)

def sort(list,left,right):
    # 如果左索引大于右索引，直接返回
    if left > right:
        return list;

    i = left
    j = right
    key = list[left]


    while(i < j and list[right] <= key):
        j -= 1
    while(i< j and list[left] >= key):
        i += 1
    if i < j:
       list[left],list[right] = list[right],list[left]

    # list = exchange(list,left,i)
    list[left],list[i] = list[i],list[left]
    # 下一次迭代
    sort(list, left, i - 1); # 左半边
    sort(list, j + 1, right); # 右半边
    print('list====',list)

def exchange(list,left,right):
    a = list[left]
    list[left] = list[right]
    list[right] = a
    return list

if __name__ == '__main__':
    list = [1,5,2,7,43,234,745,12,34,5643,564,123,4,12,34,2346,2,34]
    list1 = sort(list,0,len(list)-1)
    print('list1===',list1)