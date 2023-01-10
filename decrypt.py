
def definish():
	print('Done!', 'Decription is finished')

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

#perform decryption
def decrypt():

	#get the text files that contains encrypted values
		char_list = [ch for ch in (open("enfile.txt").read()).split(';')]

		#get the lenght of string
		length = (len(char_list)) 
		lst = []
        
        #get each values of character
		char_list.pop(length-1)
		length = (len(char_list)) 
		for iamgettingmad in range(0, length):
			k = char_list[iamgettingmad]
			k = int(k)
			char_list[iamgettingmad] = k
		for i1 in range(len(char_list)):
			x1 = char_list[i1]
			x1 = powmod(x1, d, n)
			char_list[i1] = x1 
        
        #use the chr() function to represent the actual character given the ascii value
		num1 = [chr(char) for char in char_list]
		for items1 in num1:
			lst.append('%s' %items1)

			#print value to terminal
		print(lst)
decrypt()
