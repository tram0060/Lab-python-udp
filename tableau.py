"""#BYTES

data = b"ABC" 
print(data)           
print(data[0])   
print(chr(data[0]))


#Bytesarray

data = bytearray(b"ABC")  
print(bytes(data))    
data[0] = 66 


#slicing (tranches) 
data = b"ABCDEFG" 
print(data[0:3])   
print(data[3:])  

"""
#XOR pour inverser un bit 
x = 0b01010101 
y = x ^ 0b00000001 
print(bin(x), bin(y))

ba = bytearray(b"A")    
ba[0] ==  1 
print(bytes(ba))  

