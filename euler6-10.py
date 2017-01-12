"""Problem 6
Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum."""

def sum_square_difference():
	sums_squared = (sum(i for i in xrange(1, 101))**2)
	squares_summed = sum((x**2 for x in xrange(1,101)))
	return sums_squared - squares_summed

"""Problem 7
What is the 10 001st prime number?"""

def prime(n):
	primes = [2]
	test = 3
	while len(primes) < n:
		if all(test % prime != 0 for prime in primes):
			primes.append(test)
		test += 2
	return primes[-1]

"""Problem 8
Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. 
What is the value of this product?"""

def largest_product():
	num = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444871381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
	largest = 0
	for i in range(len(num) - 13):
		product = 1 
		for j in range(i, i+13):
			product *= int(num[j: j+1])
		if product > largest:
			largest = product
	return largest

"""Problem 9
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc. """

def triplet_check(a,b,c):
	return (a**2 + b**2 == c**2)

def special_pythagorean():
	SUM = 1000
	for i in range(1, SUM):
		for j in range(i+1, SUM):
			k = SUM - (i + j)
			if triplet_check(i,j,k):
				if sum([i,j,k]) == 1000:
					print i*j*k

"""Problem 10
Find the sum of all the primes below two million."""

def sum_primes():
    primes = []
    for n in xrange(2, 2000001):
        for p in primes:
            if n % p == 0: 
            	break     
            if n < p**2:
               primes.append(n)      
               break
        else: primes.append(n)     
    return sum(primes)





