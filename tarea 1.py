from random import*
Fitness = 120


a=0
c=0
y=int(input("Ingrese la cantidad de individuos: "))
Gen= range(1,25)
x = []
e = []
z=[]
fitness = []
sums = []
u = 0
for i in range(0,y): 
    s = sample(Gen,k=15)
    x.append(s)
    #for i in range(15):
     #   for j in range(y):
      #      z = x[i][j]
       #     fitness.append(z)
        #    r = fitness[j] + fitness[j+y]
         #   sums.append(r)
for j in range(0,y):
    if a>0:
        z.append(a)
    for i in range(0,15):
        a=a+(x[j][i])
z.append(a)
for i in range(0,y):
    e.append(abs(120-z[i]))



print(x)
print(z)
print(e) 
print(min(e))
