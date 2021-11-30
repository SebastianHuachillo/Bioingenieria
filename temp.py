from random import*
y = 8 #poblacion
while True:
    Gen =range(0,41)
    L = [sample(Gen,k=12) for i in range(y)]
    Fitness = 231
    L1 = []
    L2 = []
    L3 = []
    L4 = []
    pos_max = 0
    pos_min = 0
    for i in range(y):
        L1.append(sum(L[i]))
        #print(sum(i))
    for j in L1:
        L2.append(abs(j-Fitness))
        pos_max = L2.index(max(L2))
        pos_min = L2.index(min(L2))
    if min(L2) == 0:
        L[pos_max]=L[pos_min]
        pareja = sample(L,len(L))       
        cross = [randint(1,11) for i in range(0,len(L),2)]
        print(cross)
        #print("----------------------------")
        for i in pareja:
            print(i,"\n")
            for j in cross:
                corte = j
                L3.insert(1,i[corte:])
                if len(L3) == y:
                    pass
                    print("\n",L3)
                else:
                    pass
              
        
        break

      
  

        

