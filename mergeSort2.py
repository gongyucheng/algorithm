def merge(a, b):
   c = []
   h = j = 0
   print(a,b)
   while j<len(a) and h<len(b):
       if a[j]<b[h]:
           c.append(a[j])
           j+=1
       else:
           c.append(b[h])
           h = h + 1
   if j == len(a):
        for i in b[h:]:
            c.append(i)
   if h == len(b):
        for i in a[j:]:
            c.append(i)

   return c

def merge_sort(lists):
   if len(lists) <= 1:
       return lists
   middle = len(lists)//2
   left = merge_sort(lists[:middle])
   right = merge_sort(lists[middle:])
   return merge(left,right)

if __name__ == '__main__':
    a = [4, 7, 8, 3, 5, 9]
    print(merge_sort(a))