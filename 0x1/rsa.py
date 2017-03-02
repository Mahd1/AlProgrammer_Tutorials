def ppcm (a, b) : 
	p = a*b
	while a != b:
		if a < b : b -= a
		else : a -= b
	return p/a

def extEuclideanAlg(a, b) :
    """
    Computes a solution  to a x + b y = gcd(a,b), as well as gcd(a,b)
    """
    if b == 0 :
        return 1,0,a
    else :
        x, y, gcd = extEuclideanAlg(b, a % b)
        return y, x - y * (a // b),gcd
 
def modInvEuclid(a,m) :
    """
    Computes the modular multiplicative inverse of a modulo m,
    using the extended Euclidean algorithm
    """
    x,y,gcd = extEuclideanAlg(a,m)
    if gcd == 1 :
        return x % m
    else :
        return None

p = 5
q = 11
n = p * q
phi = ppcm(p - 1, q - 1)
e = 3
d = modInvEuclid(e,phi)

print "Public key is e = " + str(e) + ", n = " + str(n)
print "Private key is d = " + str(d) + ", n = " + str(n)