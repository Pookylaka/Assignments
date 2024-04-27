import random
import pandas as pd 
import math



def isPrime(number):
    
    if number == 2:
        
        return True
    
    if number % 2 == 0:
        
        return False
    
    sqrt = math.sqrt(number)
    
    sqrt = int(sqrt)
    
    for i in range(3, sqrt + 1, 2):
        
        if number % i == 0:
            
            return False
   
    return True




def generatePrime():
    
    num = random.randint(2, 1000)
    
    while not isPrime(num):
        
        num = random.randint(2, 1000)
    
    return num




def primitiveRoot(prime):
    
    for i in range(2, prime):
      
        powers = []
        
        for j in range(1, prime):
            
            power = (i ** j) % prime
           
            if power in powers:
               
                break
            
            powers.append(power)
        
        if len(powers) == prime - 1:
            
            return i
    
    return None

p = generatePrime()
g = primitiveRoot(p)

print("Prime number p:", p) #Prime Number

print("Primitive root g:", g) #Primitive root

a = random.randint(1, p - 1) 
print("Alice's private key:", a) #A Private Key

A = (g ** a) % p
print("Alice's public key:", A) #A Public Key

b = random.randint(1, p - 1)
print("Bob's private key:", b) #B Private Key

B = (g ** b) % p
print("Bob's public key:", B) # B Public Key

AS = (B ** a) %p #A's Secret
print("Alices Secret: ", AS)
BS = (A ** b) %p
print("Bob's Secret: ", BS)

df = pd.DataFrame({
    "Alice": [g, p, A, B, AS],
    "Eve": [g, p, A, B, ((g ** A) % p) ** B],
    "Bob": [g, p, A, B, BS]
})
df.style \
  .format(precision=3, thousands=".", decimal=",") \
  .format_index(str.upper, axis=1) \
  .relabel_index(["g", "p", "A", "B", "S"], axis=0)

print(df) 