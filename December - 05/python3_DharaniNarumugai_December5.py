fp=int(input())
cfp=fp
exp=0
sal=50000
for i in range(1,32):
    if(i%3==0 and i%5==0):
        cfp=fp+1
    elif(i%3==0):
        cfp=fp+3
    elif(i%5==0):
        cfp=fp-2
    else:
        cfp=fp
    exp=exp+(cfp*2)
print("Expenditure=",exp,sep='')
if(exp>0.1*sal):
    print('\n"EXPENDITURE EXCEEDING LIMIT"')
else:
    print('\n"EXPENDITURE WITHIN LIMIT"')