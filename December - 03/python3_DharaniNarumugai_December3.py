num=int(input())
l=input()
l=l.split("\n")
for i in range(num):
    l[i]=l[i].replace('[','')
    l[i]=l[i].replace(']','')
    l[i]=l[i].replace('"','')
    l[i]=l[i].replace(',','')
    l[i]=list(l[i])
    a=list(map(str,l[i]))
    b=" ".join(a)
    b=b.replace('',"")
    b=b.split()
    l[i]=list(map(str,b))
n = [[0 for x in range(num)] for y in range(num)]
for i in range(num):
    for j in range(num):
        if(l[i][j]=="-"):
            if i==0 and j==0:
                if(l[i+1][j]=="#"):
                    n[i][j]+=1
                if(l[i][j+1]=="#"):
                    n[i][j]+=1
                if(l[i+1][j+1]=="#"):
                        n[i][j]+=1
            elif i==0 and j==num-1:
                if(l[i][j-1]=="#"):
                    n[i][j]+=1
                if(l[i+1][j]=="#"):
                    n[i][j]+=1
                if(l[i+1][j-1]=="#"):
                    n[i][j]+=1
            elif(i==num-1 and j==0):
                if(l[i-1][j]=="#"):
                    n[i][j]+=1
                if(l[i-1][j+1]=="#"):
                    n[i][j]+=1
                if(l[i][j+1]=="#"):
                    n[i][j]+=1
            elif(i==num-1 and j==num-1):
                if(l[i][j-1]=="#"):
                    n[i][j]+=1
                if(l[i-1][j-1]=="#"):
                    n[i][j]+=1
                if(l[i-1][j]=="#"):
                    n[i][j]+=1
            elif(j==0 and i!=0 and i!=num-1):
                if(l[i-1][j]=="#"):
                    n[i][j]+=1
                if(l[i+1][j]=="#"):
                    n[i][j]+=1
                if(l[i][j+1]=="#"):
                    n[i][j]+=1
                if(l[i-1][j+1]=="#"):
                    n[i][j]+=1
                if(l[i+1][j+1]=="#"):
                    n[i][j]+=1
            elif(i==0 and j!=0 and j!=num-1):
                if(l[i][j-1]=="#"):
                    n[i][j]+=1
                if(l[i+1][j]=="#"):
                    n[i][j]+=1
                if(l[i][j+1]=="#"):
                    n[i][j]+=1
                if(l[i+1][j+1]=="#"):
                    n[i][j]+=1
                if(l[i+1][j-1]=="#"):
                    n[i][j]+=1
            elif(j==num-1 and i!=0 and i!=num-1):
                if(l[i-1][j]=="#"):
                    n[i][j]+=1
                if(l[i+1][j]=="#"):
                    n[i][j]+=1
                if(l[i][j-1]=="#"):
                    n[i][j]+=1
                if(l[i-1][j-1]=="#"):
                    n[i][j]+=1
                if(l[i+1][j-1]=="#"):
                    n[i][j]+=1
            elif(i==num-1 and j!=0 and j!=num-1):
                if(l[i][j-1]=="#"):
                    n[i][j]+=1
                if(l[i][j+1]=="#"):
                    n[i][j]+=1
                if(l[i-1][j]=="#"):
                    n[i][j]+=1
                if(l[i-1][j+1]=="#"):
                    n[i][j]+=1
                if(l[i-1][j-1]=="#"):
                    n[i][j]+=1
            else:
                if(l[i-1][j]=="#"):
                    n[i][j]+=1
                if(l[i+1][j]=="#"):
                    n[i][j]+=1
                if(l[i][j+1]=="#"):
                    n[i][j]+=1
                if(l[i][j-1]=="#"):
                    n[i][j]+=1
                if(l[i+1][j-1]=="#"):
                    n[i][j]+=1
                if(l[i+1][j+1]=="#"):
                    n[i][j]+=1
                if(l[i-1][j-1]=="#"):
                    n[i][j]+=1
                if(l[i-1][j+1]=="#"):
                    n[i][j]+=1
            n[i][j]=str(n[i][j])
        else:
            n[i][j]="#"
for i in range(num):
    if i==num-1:
        print(n[i])
    else:
        print(n[i],sep='',end=',\n')
               