import random
while True:
	val = []
	pw = ''
	try:
		length = int(input("What should be the length of the password?"))
		word = input("Do you wish to include letters in your password?").lower()
		if (word=='yes'):
			a, b, c, d=65, 90, 97, 122
			val += list(range(a,b+1))+list(range(c,d+1))
		elif (word=='no'):
				pass
		else:
			raise ValueError("Enter either Yes or No.")
		num = input("Do you wish to include numbers in your password?").lower()
		if (num=='yes'):
			e, f=48, 57
			val += list(range(e,f))			
		elif (num=='no'):
				pass
		else:
			raise ValueError("Enter either Yes or No")
		sym = input("Do you wish to include symbols in your password?").lower()
		if (sym=='yes'):
			g, h, j, k, l=33, 38, 42, 64, 95
			val += list((g,h))+[j,k,l]
		elif (sym=='no'):
				pass
		else:
			raise ValueError("Enter either Yes or No")
		i = 1
		while i <= length:
			gen = chr(random.choice(val))
			pw += str(gen)
			i +=1
		print('Generated Password is: ',pw)
		x = input('Do you wish to generate again?').lower()
		if (x=='no'):
			break
	except ValueError:
		print('Entet Valid values')