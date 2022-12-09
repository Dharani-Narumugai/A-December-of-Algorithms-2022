def maxCross(arr,l,m,h):
    sm=0
    lsum=-100
    for i in range(m,l-1,-1):
        sm=sm+arr[i]
        if sm>lsum:
            lsum=sm
    sm=0
    rsum=-100
    for i in range(m,h+1):
        sm=sm+arr[i]
        if sm>rsum:
            rsum=sm
    return max(lsum+rsum-arr[m],lsum,rsum)
def SubArraySum(arr,l,h):
    if l>h:
        return -100
    if l==h:
        return arr[l]
    m=(l+h)//2
    return max(SubArraySum(arr,l,m-1),SubArraySum(arr,m+1,h),maxCross(arr,l,m,h))
def DayNum(arr,sm):
    k=[]
    flag=0
    for i in range(0,len(arr)-1):
        testsm=0
        for j in range(i,len(arr)):
            testsm=testsm+arr[j]
            if testsm==sm:
                k.append(i+1)
                k.append(j+1)
                flag=1
                break
        if flag==1:
            break
    return k
n=int(input())
l=input()
l=l.replace('{','')
l=l.replace('}','')
l=l.replace(' ','')
l=l.split(',')
for i in range(0,len(l)):
    l[i]=int(l[i])
finalsum=SubArraySum(l,0,len(l)-1)
k=DayNum(l,finalsum)
print("Profit Value: ",finalsum,sep='')
print("Proposed days to sell: Day: ",k[0]," to Day: ",k[1],sep='')
print("Stock market Change values: {",sep='',end='')
for i in range(k[0]-1,k[1]):
    if (i==k[1]-1):
        print(l[i],'}',sep='')
    else:
        print(l[i],sep='',end=',')