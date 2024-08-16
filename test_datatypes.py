# Import required modules
import math
# Import only certain function
from cmath import phase

# Declare integer variable
var1=4
# Declare floating point variable
var2=4.0

# Perform operation with two variables
var3=var1*math.sqrt(var2)

# Print type of variable
print(var3,' is of type ',type(var3))

# Integer literal in binary
bin1=0b01010111

# Integer literal in hexadecimal
bin2=0x55

# Or operation between variables
bin3=bin1|bin2

# Print variable
print(bin3)
print(bin(bin3)) # Binary
print(hex(bin3)) # Hexadecimal


###################################
# var4 is boolean
var4=type(var3) is int
print(var4)

###################################
# Complex variables
complex1=complex(1,-1)
complex2=complex(-2,2)

# Compute magnitude and phase of variables
phase1=phase(complex1)
phase2=phase(complex2)
mag1=abs(complex1)
mag2=abs(complex2)

print(f'Phase1 is: {phase1}')
print(f'Phase2 is: {phase2}')
print(f'Magnitude1 is: {mag1}')
print(f'Magnitude2 is: {mag2}')

#######################################
str1=f'Phase1 is: {phase1}'
str2=f'Phase2 is: {phase2}'
str3=str1+str2
print(str3)
print(len(str3))


########################################
# Declare empty list
list1=[]

# Append elements to list
list1.append(5.0)
list1.append(4)

# Create list of strings
list2=["alex","juan","rigo"]

# Create list of 10000 initiliazed with zeroes
list3=[0.0]*10000

# Print some elements in declared lists
print(list1[1])
print(list2[2])
print(list3[10000])