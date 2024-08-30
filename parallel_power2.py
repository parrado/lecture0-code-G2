# Maximum power for each resistor
rPower=1/4

# Input voltage
vIn=5.0

# Ask user for number of resistors
nResistors=int(input('Enter the number of resistors: '))

R=[]

# For loop to ask resistance value for each resistor
for i in range(nResistors):
    R.append(float(input(f'Enter resistance for resistor {i+1}: ')))

# Function checkPower
# This function raises an error 
# if dissipated power exceeds rated power, 
# otherwise it returns total current.
# arguments:R, resistance values list 
#           vIin, input voltage
#           rPower, rated power of resistors
i=checkPower(R,vIn,rPower)

print(f'Total current in circuit is: {i*1000:.2f} mA')




