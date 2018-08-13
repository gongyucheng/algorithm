
def sift_down(array, start, end):
  while True:
    #设定左边子节点
    left_child = start * 2 + 1
    if left_child > end:
        return
    # 如果右边子节点存在，并且大于左边子节点,就只向右边子节点
    if left_child + 1 <= end and array[left_child + 1] > array[left_child]:
        left_child = left_child + 1

    if array[left_child] > array[start]:
        array[start],array[left_child] = array[left_child],array[start]

        start = left_child
    else:
        break


def heap_sort(list):
    #最后一个非叶子节点 //为取整
    first = len(list)//2 - 1

    for i in range(first,-1,-1):
        sift_down(list,i,len(list) - 1)
    print('第一个循环==',list)

    for end in range(len(list) - 1,0 ,-1):
        list[end],list[0] = list[0],list[end]
        sift_down(list,0,end - 1)


if __name__ == "__main__":
     array1 = [1,2]
     array1[0],array1[1] = array1[1],array1[0]

     array = [16, 7, 3, 20, 17, 8]
     print(array)
     heap_sort(array)
     print("堆排序最终结果:", array)

