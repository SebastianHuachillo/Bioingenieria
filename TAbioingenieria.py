import matplotlib.pyplot as plt
import numpy as np

mues = np.loadtxt("Grupo02_a.txt")
b = mues.size
maximo = max(mues)
minimo = min(mues)
umbral = (maximo-minimo)*0.8 + minimo
ciclo = 0
posicion = []
picosr = []
for i in range(b-2):
    if (mues[i]>mues[i+1] and mues[i]>mues[i+2] and mues[i]>=mues[i-1] and mues[i]>mues[i-2] and mues[i]>umbral):
        posicion.append(i)
        picosr.append(int(mues[i]))
        ciclo+= 1
Fm = 500
Tiempototal = (posicion[ciclo-1]-posicion[0])/Fm
Freccardprom = ((ciclo-1)*60)/Tiempototal
freccardinsta = []
Tiempototal3=[]
Tiempo =[]
for j in range(len(posicion)-1):
    Tiempototal2 = (posicion[j+1]-posicion[j])/Fm
    Tiempototal3.append((posicion[j+1]-posicion[j])/Fm)
    freccardinsta.append(round(60/Tiempototal2))
for t in range(len(Tiempototal3)-1):
    Tiempo.append(abs(Tiempototal3[t+1]-Tiempototal3[t]))
print(f"La frecuencia cardiaca promedio es: {round(Freccardprom)} bpm\n")
for f in range(len(freccardinsta)):
    print(f"La {f+1} frecuencia cardiaca instantaneas: {freccardinsta[f]} bpm")
print("\n")
for h in range(len(Tiempo)):
    if (Tiempo[h]<0.04 and (60<=round(Freccardprom) and round(Freccardprom)<=100)):
        print(f"La resta entre el ciclo {h+1} y {h+2} es menor a 40 msegundos. Ademas, su frecuencia cardiaca promedio esta dentro del rango de 60 y 100 bpm tiene un ritmo cardiaco normal")
    elif(Tiempo[h]>0.04 and (60<=round(Freccardprom) and round(Freccardprom)<=100)):
        print(f"La resta entre el ciclo {h+1} y {h+2} es mayor a 40 msegundos. Ademas, su frecuencia cardiaca promedio esta dentro del rango de 60 y 100 bpm su ritmo cardiaco es normal y arritmia")
    elif(Tiempo[h]<0.04 and round(Freccardprom)<60):
        print(f"La resta entre el ciclo {h+1} y {h+2} es menor a 40 msegundos. Ademas, su frecuencia cardiaca promedio es menor a 60 bpm su ritmo es bradicardia")
    elif(Tiempo[h]>0.04 and round(Freccardprom)<60):
        print(f"La resta entre el ciclo {h+1} y {h+2} es mayor a 40 msegundos. Ademas, su frecuencia cardiaca promedio es menor a 60 bpm su ritmo es bradicardia y arritmia")
    elif(Tiempo[h]<0.04 and round(Freccardprom)>100):
        print(f"La resta entre el ciclo {h+1} y {h+2} es menor a 40 msegundos. Ademas, su frecuencia cardiaca promedio es mayor a 100 bpm su ritmo cardiaco es taquicardia")
    elif(Tiempo[h]>0.04 and round(Freccardprom)>100):
        print(f"La resta entre el ciclo {h+1} y {h+2} es mayor a 40 msegundos. Ademas, su frecuencia cardiaca promedio es mayor a 100 bpm su ritmo cardiaco es taquicardia y arritmia")   
G = 200
Vrefh = 3.3
Vrefl = 0
bits = 10
vx = 0 
tie50ms =int(Fm*0.05)
s=[]
vp =[]
pos_s=[]
pos_q = []
punto_l = []
punto_h = []
q = []
t = []
for i in range(len(posicion)):
    picos1 = posicion[i]-tie50ms
    q_r =[]
    pos_q1 = []
    for j in range(tie50ms):
        q_r.append(mues[picos1+j])
    for h in range(0,len(q_r)):
        if mues[picos1+h]<=mues[picos1+h-1] and mues[picos1+h]<=mues[picos1+h-3] and mues[picos1+h]<=mues[picos1+h+1] and mues[picos1+h]<=mues[picos1+h+3] and mues[picos1+h]<umbral:
            pos_q1.append(picos1+h)
    pos_q.append(pos_q1[-1])
for i in range(len(pos_q)):
    q.append(int(mues[pos_q[i]]))

for i in range(0,len(posicion)):
    pl = posicion[i]-tie50ms
    ph = posicion[i]+tie50ms
    punto_l.append(int(posicion[i]-tie50ms))
    punto_h.append(int(posicion[i]+tie50ms))
    s.append(min(mues[pl:ph]))
minimoqs=min(q,s)
for i in range(0,len(posicion)):
    aux=[]
    aux2=[]
    for j in range(punto_l[i], punto_h[i]):
        aux.append(int(mues[j]))
        aux2.append(j)
    pos_s.append(aux2[aux.index(s[i])])
    aux.clear()
for i in range(len(picosr)):
    vp.append((((picosr[i]-minimoqs[i])*(Vrefh-Vrefl))/(pow(2,10)))*(1/G)*1000)
print("\n")
for i in range(len(vp)):
    print(f"La Amplitud QRS {i+1} es {vp[i]:.2f} mV")
for i in range(len(posicion)):
    t.append(((pos_s[i]-pos_q[i])/Fm)*1000)
print("\n")
for i in range(len(t)):
    print(f"La duracion QRS {i+1} es {t[i]:.2f} ms")
plt.plot(mues)
plt.title("Señal de Electrocardiograma ECG")
plt.axhline(umbral,color="r",linestyle="--")
plt.show()
