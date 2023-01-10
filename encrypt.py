
def enfinish():
	print('Done!', 'Encryption is finished')

		#Function perform decryption given the e,d and n values
def powmod(b, e, m):
    #TODO why it is much faster than the traditional method ?
	b2 = b
	res = 1
	while e:
		if e & 1:
			res = (res * b2) % m   
		b2 = (b2*b2) % m        
		e >>= 1                 
	return res

#message to encrypt
message = 'hello'

#get values of e,d and n stored in .pem files
efile = open('efile.pem', 'r')
e = int(efile.read())
efile.close()
dfile = open('dfile.pem', 'r')
d = int(dfile.read())
dfile.close()
   
nfile = open('nfile.pem', 'r')
n = int(nfile.read()) 
nfile.close()

#perform encryption
def encrypt():

	      #get each character from string
		char_list = [ch for ch in message]

		#get the ascii value of character
		num = [ord(char) for char in char_list]
		for i in range(len(num)):
			x = num[i]
			x = powmod(x, e, n)
			num[i] = x 

			#store value of character in .txt file
		with open('enfile.txt', 'w') as filehandle:
                    #make it .pem file than .txt for good
			for items in num:
				filehandle.write('%s; ' %items)

				#print encrypted values
				print(items)
		enfinish()
encrypt()
