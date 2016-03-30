import random
import time

class Matrix:
    m = ((0,0),(0,0))

    def __init__(self, r1=None, r2=None):
        self.m = ((0,0) if r1 == None else r1, (0,0) if r2 == None else r2)

    def __str__(self):
        return "(({0},{1}),({2},{3}))".format(self.m[0][0], self.m[0][1],
                                              self.m[1][0], self.m[1][1]) 

    def __mul__(self, other):
        return Matrix((self.m[0][0]*other.m[0][0] + self.m[0][1]*other.m[1][0],
                       self.m[0][0]*other.m[0][1] + self.m[0][1]*other.m[1][1]),
                      (self.m[1][0]*other.m[0][0] + self.m[1][1]*other.m[1][0],
                       self.m[1][0]*other.m[0][1] + self.m[1][1]*other.m[1][1]))

primes = []
testPrime = 2

def isPrime(p) :
    for i in primes:
        if i * i > p:
            return True
        if p % i == 0:
            return False

    i = testPrime
    while i * i <= p:
        if p % i == 0:
            return False
        i += 1
    return True

while len(primes) < 100000:
    while not isPrime(testPrime):
        testPrime += 1
    primes.append(testPrime)
    testPrime += 1

def getLargeRandomPrime(bits):
    test = random.getrandbits(bits) + 2 ** bits
    while not isPrime(test):
        test = test + 1
    return test

for i in range(1,100):
    start = time.time()
    print i, getLargeRandomPrime(i), getLargeRandomPrime(i), time.time() - start

p = 16712248341883957
q = 15473411525812663

n = p * q
eu = n - (p + q - 1)
e = 65537

def getInverse(a, m):
    A = Matrix((1,0),(0,1))
    R = Matrix((a,m),(1,0))
    while not R.m[0][1] == 0:
        q = R.m[0][0] // R.m[0][1]
        Q = Matrix((0,1),(1,-q))
        A = A * Q
        R = R * Q
    inverse = A.m[0][0]
    return inverse if inverse > 0 else inverse + m

d = getInverse(e,eu)

def power(a,b,c):
    if b == 0:
        return 1;
    if b == 1:
        return a
    return power(a * a % c, b//2, c) * power(a, b % 2, c) % c

def encrypt(m):
    return power(m,e,n)

def decrypt(m):
    return power(m,d,n)

print e,d,n

for i in range(2,100):
    m = encrypt(i)
    print i, m, decrypt(m)
