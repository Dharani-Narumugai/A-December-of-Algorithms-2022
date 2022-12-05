n=int(input())
my_vars={}
l={}
for i in range(n):
    var_name = "var%d"%i
    l_name="l%d"%i
    my_vars[var_name]=input()
    my_vars[var_name]=my_vars[var_name].replace('{','')
    my_vars[var_name]=my_vars[var_name].replace('}','')
    my_vars[var_name]=my_vars[var_name].replace("'","")
    my_vars[var_name]=my_vars[var_name].replace(' ','')
    my_vars[var_name]=my_vars[var_name].replace(',','')
    l[l_name]=[]
    sub=""
    for m in range(len(my_vars[var_name])):
        sub+=my_vars[var_name][m]
        if(m%2!=0 and sub!=""):
            l[l_name].append(sub)
            sub=""
for i in range(n):
    l_name="l%d"%i
    for j in l[l_name]:
        print(chr(int(j,16)),sep='',end='')
    print()

