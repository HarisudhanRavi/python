#getting required data from user
n=int(input('Enter the total number of units to be committed\n'))
MA=[]
MI=[]
INH=[]
NLC=[]
SC=[]
INC=[]
ONOFF=[]
FC=float(input('Enter the fuel cost in Rs/MBtu\n'))
LOAD=int(input('Enter the demand in MW\n'))
for i in range(n):
    if i==0:
        print('Enter the following details of the ',i+1,'st unit:\n')
    elif i==1:
        print('Enter the following details of the ',i+1,'nd unit:\n')
    elif i==2:
        print('Enter the following details of the ',i+1,'rd unit:\n')
    else:
        print('Enter the following details of the ',i+1,'th unit:\n')
    A=float(input('Maximum power of in MW:\n'))
    B=float(input('Minimum power of in MW:\n'))
    C=float(input('Incremental heat rate of in Btu/MWhr:\n'))
    D=float(input('No load cost of in Rs/hr:\n'))
    E=float(input('Start up cost of in Rs:\n'))
    F=float(input('Incremental cost in Rs/MWhr:\n'))
    G=float(input('Enter the unit is either on/off at starting.If on,enter 1.If off,enter 0\n'))
    MA.append(A)
    MI.append(B)
    INH.append(C)
    NLC.append(D)
    SC.append(E)
    INC.append(F)
    ONOFF.append(G)

#FLAPC calculation
FLAPC=[]
for i in range(n):
    f=((INH[i]*MA[i]*FC)+NLC[i])/MA[i]
    FLAPC.append(f)
for i in range(n):
    if ONOFF[i]==1:
        SC[i]=0


#priority list
#sorting all data depending on priority list
ma=[MA for _,MA in sorted(zip(FLAPC,MA))]
mi=[MI for _,MI in sorted(zip(FLAPC,MI))]
inh=[INH for _,INH in sorted(zip(FLAPC,INH))]
nlc=[NLC for _,NLC in sorted(zip(FLAPC,NLC))]
sc=[SC for _,SC in sorted(zip(FLAPC,SC))]
inc=[INC for _,INC in sorted(zip(FLAPC,INC))]
onoff=[ONOFF for _,ONOFF in sorted(zip(FLAPC,ONOFF))]
flapc=FLAPC.copy()
flapc.sort()


#on/off binary table
matrix=[]
for i in range(n): 
    matrix.append([]) 
    for j in range(n): 
        if i>=j:
            matrix[i].append(1)
        else:
            matrix[i].append(0)
print(matrix)

#feasibility
x=[i for i in range(len(onoff)) if onoff[i]==1]


#change binary table based on feasibility
for a,b in enumerate(matrix):
    for b in x:
        if matrix[a][b]==0:
            matrix.remove(matrix[a])

print(matrix)
#power distribution plam
Mi=[mi for i in range(len(matrix))]
Ma=[ma for i in range(len(matrix))]
for a in range(len(matrix)):
    for b in range(n):
        if matrix[a][b]==0:
            Mi[a][b]=0
p=Mi
for a in range(len(matrix)):
    for b in range(n):
        if sum(p[a])>LOAD:
            pass
        else:
            if Ma[a][b]-Mi[a][b]>=LOAD-sum(p[a]):
                p[a][b]=Mi[a][b]+LOAD-sum(p[a])
                break
            elif Ma[a][b]-Mi[a][b]<LOAD-sum(p[a]):
                p[a][b]=Ma[a][b]


#calculating pcost,scost,fcost
pcost=[]
scost=[]
fcost=[] 
for i in range(len(matrix)):
    for j in range(n):
        if matrix[i][j]==1:
            a+=p[i][j]*inc[j]+nlc[j]
            b+=sc[j]*1
        c=a+b
    pcost.append(a)
    scost.append(b)
    fcost.append(c)


#getting ouput based on fcost
x=fcost.index(min(fcost))
ans=[]
for i in range(n):
    if matrix[x][i]==1:
        a=flapc[i]
        ans.append(a)


print('The units to be on are\n')
for i in range(n):
    for j in ans:
        if FLAPC[i]==j:
            print('Unit ',i+1,'\n')








            
