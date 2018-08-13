

def sort(list):
    #设定增量,依次除以2
   d = int(len(list)/2)

   while(d >= 1):
        for i in range(d,len(list)):
            x = list[i]

            #取增量前的数据
            j = i - d
            while(j >= 0 and x < list[j]):
                #所有数据往后移动  按增量移动
                list[j + d] = list[j]
                j = j - d
            #数据插入到相应的位置后面
            list[j+d] = x
        d = int(d/2)
   return list
if __name__ == '__main__':
    list = [7,223421,50,3,84,4,1,9,645,7568,9657,1231]

    list1 = sort(list)
    print('list1===',list1)