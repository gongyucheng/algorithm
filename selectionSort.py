def sort(list):
    minIndex = 0
    for i in range(0,len(list) - 1):
        minIndex = i
        for j in range(i+1,len(list)):
            if list[j] < list[minIndex]:
                minIndex = j

        list[i],list[minIndex] = list[minIndex],list[i]

    return list

if __name__ == '__main__':
    list = [7,223421,50,3,84,4,1,9,645,7568,9657,1231]

    list1 = sort(list)
    print('list1===',list1)