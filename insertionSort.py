
aa = [7,3,8,6,1,9,2]
len = len(aa)
tem = 0
for i in range(1,len):
    tem = aa[i]
    j = i - 1
    while(j>=0 and tem <= aa[j]):
        aa[j+1] = aa[j]
        j -= 1
    aa[j+1] = tem

print(aa)
