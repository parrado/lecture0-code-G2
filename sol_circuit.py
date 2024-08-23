# Constants definition
nLoads=4
iMax=20
vIn=170

# List to store power for each load
#p=[0.0]*nLoads
p=[]

# For loop to ask powers
for i in range(nLoads):
    #p[i]= float(input(f'Ingrese la potencia de la carga {i+1}: '))
    p.append(float(input(f'Ingrese la potencia de la carga {i+1}: ')))

#print(p)

# Variable to store total current
iTotal=0.0

# For loop to compute total current
for j in range(len(p)):
    i=p[j]/vIn
    iTotal=iTotal+i

# If overcurrent detected
if iTotal>=iMax:
    print(f'El breaker se disparó, la corriente es {iTotal}A !!!')
else: # If everything is ok
    print(f'Hasta ahora todo bien, la corriente es {iTotal}A!!')