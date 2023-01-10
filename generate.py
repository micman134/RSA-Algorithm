import random

#ensures that public keys meets the coprime conditions
def coprime(a, b):
    while b != 0:
        a, b = b, a % b
    return a
   
#used for mod operations of private key
def modInverse(a, m) : 
    a = a % m
    for x in range(1, m) : 

        if ((a * x) % m == 1) : 

            return x

#calls the mod function for its operations
def modinv(a, m):
	d = modInverse(a, m)
	return d

#two prime numbers P and Q
p = 13
q = 17

#n is used to get the public and private key
n = p * q

#phi is used to check if the value of e is a coprime of n
phi = (p-1) * (q-1)

#generates random numbers for e
e = random.randrange(1, phi)
g = coprime(e, phi)

#continous chcks the value of e to meet the condition  
while g != 1:
    e = random.randrange(1, phi)
    g = coprime(e, phi)


#Use Extended Euclid's Algorithm to generate the private key
d = modinv(e, phi)

#public and private key
publicKey = (e, n)
privateKey = (d, n)


#saving the values of n, d and e for further use	
efile = open('efile.pem', 'w')
efile.write('%d' %(int(e)))
efile.close()
   
dfile = open('dfile.pem', 'w')
dfile.write('%d' %(int(d)))
dfile.close()
   
nfile = open('nfile.pem', 'w')
nfile.write('%d' % (int(n)))
nfile.close()

#print values of public and private key
print('Public key:', publicKey)
print('Private keys:', privateKey)

