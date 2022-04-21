import math
import random

# Generating Random Prime Numbers for P and Q
def Generating_P_and_Q_values():
    while(1):
      flag = 0
      Prime_Number = random.randint(32768, 65535) # values should be in between 2**15+1, 2**16-1 (16 bit)
      for i in range(1, Prime_Number):
         if (Prime_Number % i == 0):
            flag = flag + 1
      if (flag ==1):
         return Prime_Number

P = Generating_P_and_Q_values()
print ("\n Random P Value: ",P)

Q = Generating_P_and_Q_values()
print (" Random Q Value: ",Q)

n = P * Q
print ('\n n = P * Q =', n)

PHI= (P-1)*(Q-1)
print ('\n ϕ(n) = (P-1)*(Q-1) = ', PHI)


# Selecting "e" value based on ϕ(n)
def Generating_encryption_key_e(PHI):
  while(1):
      HalfPHI= round(PHI/2)
      e = random.randint(11, 65535)
      e = (e*2) +1
      if (e%2 == 1 and e < PHI):
         x = PHI
         y = e
         while(y):
             x,y = y, x%y
             if(y == 1):
                 return e
e = Generating_encryption_key_e(PHI)

if(e<PHI):
    print("\n Value of ϕ(n) is:", PHI)
    print(' The GCD of e and ϕ(n):', math.gcd(e, PHI))
    print(" and Value of e < ϕ(n)")
    print(" Value of e is:", e)

# Calculating the Secret key or the Decryption key"d", such that (e*d) mod Phi(N)=1
def Generating_decryption_key_d(e,PHI):
    d = pow(e, -1, PHI)

    v = pow(e * d, 1, PHI)
    print(' (e*d)modϕ(n) :', v)
    print(' Value of d is :', d)

d= Generating_decryption_key_d(e, PHI)

