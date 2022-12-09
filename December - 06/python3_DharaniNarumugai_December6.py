pos=int(input("Position: "))
l=input("Set of numbers: ")
l=l.split()
for i in range(len(l)):
    l[i]=int(l[i])
k=[]
k.append(input("Player going first: "))
if k[0]=="Tanika":
    k.append("Bob")
else:
    k.append("Tanika")
while(l[0]!=0):
    k[0],k[1]=k[1],k[0]
    l[0]-=1
    l[0],l[pos-1]=l[pos-1],l[0]
print(k[1]," wins the game!","\n",k[0]," loses the game!",sep='')