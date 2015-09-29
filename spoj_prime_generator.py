# import math
# for t in range(int(input())):
#     m,n=[int(x) for x in input().split()]
#     for num in range(m,n+1):
#         prime = True
#         for i in range(2,int(math.sqrt(num))+1):
#             if (num%i==0):
#                 prime = False
#         if prime:
#             print (num)
#     print("\n")
    
# import math
# for num in range(1,101):
#     if all(num%i!=0 for i in range(2,int(math.sqrt(num))+1)):
#        print num

'''Sieve of Eratosthense Algorithm'''
def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False
    
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False
                
z=list(primes_sieve2(10000))
for i in z:
	print(i)