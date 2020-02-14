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