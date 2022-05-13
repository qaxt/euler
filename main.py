import math

def prime(n):
  if (int(n) != n):
    return False
  for i in range(2, math.floor(math.sqrt(n)) + 1):
    if (n % i == 0):
      return False
  return True
  
def prime_factors(n: int):
  factors = []
  for i in range(2, math.floor(math.sqrt(n)) + 1):
    if (n % i == 0 and prime(i)):
      factors.append(i)
    if (n % (n/i) == 0 and prime(n/i)):
      factors.append(n/i)
  if (prime(n)):
    factors.append(n)
  return factors

def highest_prime_factor(n: int):
  factors = []
  for i in range(2, math.floor(math.sqrt(n)) + 1):
    if (n % (n/i) == 0 and prime(n/i)):
      return n/i
    if (n % i == 0 and prime(i)):
      factors.append(i)
  return max(factors)

print(highest_prime_factor(600851475143))