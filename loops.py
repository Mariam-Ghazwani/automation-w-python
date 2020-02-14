#example 1
x = 0
while x < 5:
  print("Not there yet, x=" + str(x))
  x = x + 1
print("x=" + str(x))

#example2
def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
    
attempts(5)

#example3
def count_down(start_number):
  current = start_number
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)

#example 4 not zero and not even
while x != 0 and x % 2 == 0:
  x = x/2

#example 5
def smallest_prime_factor(x):
    """Returns the smallest prime number that is a divisor of x"""
    # Start checking with 2, then move up one by one
    n = 2
    while n <= x:
        if x % n == 0:
            return n
        n += 1

print(smallest_prime_factor(12)) # should be 2
print(smallest_prime_factor(15)) # should be 3

# example 6
def sum_divisors(n):
  # Return the sum of all divisors of n, not including n
  d = 1
  summa = 0
  
  while d < n:
    if n % d == 0:
        summa = summa + d
        d = d + 1
    else:
        d = d + 1
  return summa

print(sum_divisors(6)) # Should be 1+2+3=6
print(sum_divisors(12)) # Should be 1+2+3+4+6=16

# example w/for loop 1

def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum

print(sum_squares(10)) # Should be 285

# example w/for loop 2

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result = result*i
    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120