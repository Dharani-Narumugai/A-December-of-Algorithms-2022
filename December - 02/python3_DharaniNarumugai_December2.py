name=input()
l=list(name)
l.pop()
l.pop()
for i in range(2):
    j=l.pop()
    l.insert(0,j)
for i in l:
    print(i,sep='',end='')
