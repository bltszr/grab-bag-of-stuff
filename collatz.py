def collatz(n):
	while n!=1:
		if n%2==0:
			n=n/2
			yield(n)
		else:
			n=(3*n)+1
			yield(n)

print(len(list(collatz(9**98))))